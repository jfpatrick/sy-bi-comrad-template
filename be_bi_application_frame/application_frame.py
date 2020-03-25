
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QIcon

from papc.interfaces.pyjapc import SimulatedPyJapc
from papc.system import System

from be_bi_application_frame.resources.ui_application_frame import Ui_Form as Ui_ApplicationFrame


class ApplicationFrame(QWidget, Ui_ApplicationFrame):
    """
    The Application Frame containing a LogBox, a Timing Widget and a RBAC Button.
    You can set you form as Centra Widget by calling .setCentralWidget(). No further setup required.

    The LogBox hooks automatically to the application's logger, so no setup is required.
    The Timing Widget will be added as soon as it comes out.
    The RBAC button will be replaced with a working version based on PyJAPC until a proper solution comes out.
    """
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Empty Application Frame")
        self.setWindowIcon(QIcon('resources/images/CERN_logo.png'))
        self.central_widget = self.central_widget_container.findChild(QLabel, "placeholder")

        # Monkey-patch PyJAPC with papc
        # test_devices = System(devices=setup_papc_devices())
        # pyjapc.PyJapc = SimulatedPyJapc.from_simulation_factory(lambda: test_devices, strict=False)
        # logging.debug("Test mode is ON: pyjapc.PyJapc has been replaced by {}".format(pyjapc.PyJapc))

    def setCentralWidget(self, widget):
        self.central_widget = widget
        self.central_widget_container.layout().replaceWidget(
            self.central_widget_container.findChild(QLabel, "placeholder"), widget)
