from datetime import datetime

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication

import pyjapc
from accwidgets.graph import UpdateSource, PointData

from be_bi_application_frame.models.papc_setup.papc_devices import setup_papc_devices

# Monkey-patch PyJAPC with papc - connect to simulated devices instead of real devices
# Remove this line to connect to real devices
pyjapc.PyJapc = setup_papc_devices()


class DummyAppModel(QObject):

    def __init__(self):
        super(QObject, self).__init__()
        self.japc = pyjapc.PyJapc()
        self.japc.setSelector("LHC.USER.ALL")

    def get_amplitude_sin(self):
        return self.japc.getParam("TEST_DEVICE/Settings#amplitude_sin")

    def get_period_sin(self):
        return self.japc.getParam("TEST_DEVICE/Settings#period_sin")

    def get_amplitude_cos(self):
        return self.japc.getParam("TEST_DEVICE/Settings#amplitude_cos")

    def get_period_cos(self):
        return self.japc.getParam("TEST_DEVICE/Settings#period_cos")

    @pyqtSlot(int)
    def set_amplitude_sin(self, value):
        self.japc.setParam("TEST_DEVICE/Settings#amplitude_sin", value)

    @pyqtSlot(int)
    def set_period_sin(self, value):
        self.japc.setParam("TEST_DEVICE/Settings#period_sin", value)

    @pyqtSlot(int)
    def set_amplitude_cos(self, value):
        self.japc.setParam("TEST_DEVICE/Settings#amplitude_cos", value)

    @pyqtSlot(int)
    def set_period_cos(self, value):
        self.japc.setParam("TEST_DEVICE/Settings#period_cos", value)


class DeviceTimingSource(UpdateSource):

    def __init__(self, parameter_name, selector):
        super().__init__()
        self.japc = pyjapc.PyJapc()
        self.japc.setSelector(timingSelector=selector)
        self.japc.subscribeParam(parameter_name, self._new_value_received)
        self.japc.startSubscriptions()

    def _new_value_received(self, _, value) -> None:
        self.sig_new_timestamp.emit(datetime.now().timestamp())


class SinglePointSource(UpdateSource):

    def __init__(self, parameter_name, selector):
        super().__init__()
        self.parameter_name = parameter_name
        self.selector = selector
        self.japc = pyjapc.PyJapc()
        self.japc.setSelector(timingSelector=selector)
        self.japc.subscribeParam(parameter_name, self._create_new_value)
        self.japc.startSubscriptions()

    def _create_new_value(self, _, value) -> None:
        new_data = PointData(
            x=datetime.now().timestamp(),
            y=float(value)
        )
        # ### Small workaround for passing QObject derived classes through signals
        new_data.moveToThread(QApplication.instance().thread())
        new_data.setParent(self)
        # ### End of workaround
        self.sig_new_data[PointData].emit(new_data)
