"""
For reference, see:
https://acc-py.web.cern.ch/gitlab/bisw-python/pyqt-tutorial/docs/stable/2-project-structure.html#project-name-models
"""
import math
from datetime import datetime

from PyQt5.QtCore import QObject, pyqtSlot

import pyjapc
from accwidgets.graph import UpdateSource, PointData

#########################################################################################
# See https://acc-py.web.cern.ch/gitlab/bisw-python/pyqt-tutorial/docs/stable/2-project-structure.html#project-name-models-papc-setup
# Monkey-patch PyJAPC with papc - connect to simulated devices instead of real devices
# UNCOMMENT THESE LINES TO CONNECT WITH A SIMULATED DEVICE
#
# from sy_bi_pyqt_template.models.papc_setup.papc_devices import setup_papc_devices
# pyjapc.PyJapc = setup_papc_devices()
#########################################################################################


class SpinBoxModel(QObject):
    """
    This class acts as Model for the ``SpinBox`` below the plot.
    It connects to PyJAPC and performs GET and SET operations.

    Functions decorated with the @pyqtSlot decorator can be connected to signals coming from the View.
    You can see how the signals and the slots are connected in the ``MainWidget`` class.
    """
    def __init__(self):
        super(QObject, self).__init__()
        # Create the PyJAPC connector
        self.japc = pyjapc.PyJapc()
        # Use the empty selector
        self.japc.setSelector("")

    def get_frequency(self) -> float:
        """
        GETs the frequency from the control system through PyJAPC.
        :return: the frequency (int)
        """
        return self.japc.getParam("BISWRef1/Settings#frequency")

    @pyqtSlot(int)
    def set_frequency(self, value: int) -> None:
        """
        SETs the frequency to the control system through PyJAPC.
        Note: this function is a Slot: therefore it can receive updates from the View.
        Such updates do not reach with a direct call, but are sent by emitting a signal.
        :param value: the frequency to set
        :return: None
        """
        self.japc.setParam("BISWRef1/Settings#frequency", value)


class SinglePointSource(UpdateSource):
    """
        This class acts as a Data model for a plot.
        It subscribes to JAPC and emits a signal carrying a new PointData instance every time it receives new data.
        Such signal will be received by the View, which will react accordingly.

        In this specific case, the ``sig_new_data`` signal can be understood by accwidgets' ``PlotWidget`` classes.
        Always check the documentation to make sure which signal names are understood by which target classes.
    """
    def __init__(self, parameter_name, selector):
        super().__init__()
        # Create the PyJAPC connector
        self.japc = pyjapc.PyJapc()
        # Use the given selector
        self.japc.setSelector(timingSelector=selector)
        # Subscribe to the requested Device/Property#field
        self.japc.subscribeParam(parameter_name, self._create_new_value)
        # Start receiving data
        self.japc.startSubscriptions()

    def _create_new_value(self, name: str, value: float) -> None:
        """
        Function called every time PyJAPC receives a new value.
        It emits the signal ``sig_new_data``, that carries a ``PointData`` instance.

        The ``PointData`` instance contains the new value as Y coordinate and the timestamp of reception
        as the X coordinate.  It will be added to the plot as part of a curve.

        :param name: Always equal to parameter_name - uninteresting, it never changes in this case.
        :param value: The new value received, to be emitted as the Y coordinate of the output ``PointData``
        :return: None
        """
        new_data = PointData(
            x=datetime.now().timestamp(),
            y=float(math.sin(value/10))
        )
        self.sig_new_data[PointData].emit(new_data)
