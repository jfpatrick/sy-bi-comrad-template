import math
import threading
import logging
from datetime import datetime

from PyQt5.QtCore import QTimer

import pyjapc
from accwidgets.graph import UpdateSource, PointData

from be_bi_application_frame.demo.papc_devices import setup_papc_devices

# Monkey-patch PyJAPC with papc - connect to simulated devices instead of real devices
pyjapc.PyJapc = setup_papc_devices()


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
        self.japc = pyjapc.PyJapc()
        self.japc.setSelector(timingSelector=selector)
        self.japc.subscribeParam(parameter_name, self._create_new_value)
        self.japc.startSubscriptions()

    def _create_new_value(self, _, value) -> None:
        new_data = PointData(
            x=datetime.now().timestamp(),
            y=float(value)
        )
        print(threading.currentThread().getName())
        self.sig_new_data[PointData].emit(new_data)


class LocalTimerTimingSource(UpdateSource):

    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._create_new_value)
        self.timer.start(1000 / 60)

    def _create_new_value(self) -> None:
        self.sig_new_timestamp.emit(datetime.now().timestamp())


class SinusCurveSource(UpdateSource):

    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._create_new_value)
        self.timer.start(1000 / 30)

    def _create_new_value(self) -> None:
        new_data = PointData(
            x=datetime.now().timestamp(),
            y=math.sin(datetime.now().timestamp()),
        )
        self.sig_new_data[PointData].emit(new_data)
