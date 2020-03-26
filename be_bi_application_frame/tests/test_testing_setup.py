import math
import pyjapc

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtGui import QIcon


def test_can_use_qt(qtbot):
    """ Makes sure there are no problems with Qt in general, unrelated with the actual application. """
    class TestWindow(QTabWidget):
        def __init__(self, parent=None):
            super(TestWindow, self).__init__(parent)
            self.resize(1366, 900)
            self.setWindowTitle("Test Window")
            self.setWindowIcon(QIcon('resources/images/CERN_logo.png'))

    main_window = TestWindow()
    main_window.show()
    qtbot.addWidget(main_window)
    assert main_window is not None


def test_can_use_pyjapc(mock_pyjapc):
    """ Makes sure there are no problems mocking PyJapc, unrelated with the actual application. """
    japc_ppm = pyjapc.PyJapc()
    japc_ppm.setSelector(timingSelector="LHC.USER.ALL")
    japc_ppm.setParam("TEST_DEVICE/Settings", {'theta': 1, 'amplitude': 3})
    value = japc_ppm.getParam("TEST_DEVICE/Acquisition#sin")
    assert value is not None
    assert value == math.sin(1) * 3


def test_can_use_pyjapc_within_qt(mock_pyjapc, qtbot):
    """ Makes sure there are no problems with mocking PyJapc within a Qt application. """
    class TestWindow(QTabWidget):
        def __init__(self, parent=None):
            super(TestWindow, self).__init__(parent)
            self.resize(1366, 900)
            test_can_use_pyjapc(mock_pyjapc)
            self.setWindowTitle("Test Window")

    main_window = TestWindow()
    main_window.show()
    qtbot.addWidget(main_window)
    assert main_window is not None
    assert main_window.windowTitle() == "Test Window"
