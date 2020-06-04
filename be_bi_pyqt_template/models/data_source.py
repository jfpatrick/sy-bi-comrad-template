import math
from datetime import datetime

from PyQt5.QtCore import QObject, pyqtSlot

import pyjapc
from accwidgets.graph import UpdateSource, PointData

#########################################################################################
# Monkey-patch PyJAPC with papc - connect to simulated devices instead of real devices
# UNCOMMENT THESE LINES TO CONNECT WITH A SIMULATED DEVICE
# from be_bi_pyqt_template.models.papc_setup.papc_devices import setup_papc_devices
# pyjapc.PyJapc = setup_papc_devices()
#########################################################################################


class ExampleModel(QObject):
    """
    This class acts as Model for the ``SpinBox`` below the plot.

    It connects to PyJAPC and performs GET and SET operations.

    Functions decorated with the @pyqtSlot decorator can be connected to signals coming from the View.
    In general, **no direct call from the View to the Model, or from the Model to the View, should ever happen**.

    You can see how the signals and the slots are connected in the ``ExampleWidget`` class.
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
        Note: this function is a Slot: therefore it can receive direct updates from the View.
        The View however has no knowledge of this function: is the Presenter (``ExampleWidget``) that wires them
        together shortly after instantiation.
        :param value: the frequency to set
        :return: None
        """
        self.japc.setParam("BISWRef1/Settings#frequency", value)


class DeviceTimingSource(UpdateSource):
    """
        This class acts as a Timing model for a plot.

        It subscribes to JAPC and emits a new timestamp every time it receives new data.

        Qt Signals can be picked up by the View, once the Presenter (``ExampleWidget``) sets them up.

        In this specific case, the ``sig_new_timestamp`` signal can be understood by accwidgets' ``PlotWidget`` classes.
        Always check the documentation to make sure which signal names are understood by which target classes.
    """
    def __init__(self, parameter_name, selector):
        """
        Instantiate the object, creates its own PyJAPC connector and subscribes to the requested value.
        :param parameter_name:
        :param selector:
        """
        super().__init__()
        # Create the PyJAPC connector
        self.japc = pyjapc.PyJapc()
        # Use the given selector
        self.japc.setSelector(timingSelector=selector)
        # Subscribe to the requested Device/Property#field
        self.japc.subscribeParam(parameter_name, self._new_value_received)
        # Start receiving data
        self.japc.startSubscriptions()

    def _new_value_received(self, name: str, value: int) -> None:
        """
        Function called every time PyJAPC receives a new value.
        It emits the signal ``sig_new_timestamp``, that carries a timestamp.
        :param name: Always equal to parameter_name - uninteresting, it never changes in this case.
        :param value: The new value received - uninteresting, because we need to emit only its timestamp.
        :return: None.
        """
        # Emit a signal containing the timestamp of the execution time of this function
        self.sig_new_timestamp.emit(datetime.now().timestamp())
        # NOTE: any timestamp can be emitted here: if the JAPC value carries a more meaningful timestamp,
        #   you can extract it and emit it instead.


class SinglePointSource(UpdateSource):
    """
        This class acts as a Data model for a plot.

        It subscribes to JAPC and emits a new PointData value every time it receives new data.

        Emitted signals can be in turn picked up by the View, once the Presenter (``ExampleWidget``) sets them up.

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
