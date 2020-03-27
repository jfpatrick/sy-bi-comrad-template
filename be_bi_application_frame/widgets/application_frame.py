import logging
import threading

from PyQt5.QtWidgets import QWidget, QTabWidget
from PyQt5.QtGui import QIcon

from accwidgets.graph import TimeSpan, ScrollingPlotWidget, CyclicPlotWidget

from be_bi_application_frame.models.data_source import LocalTimerTimingSource, SinusCurveSource, SinglePointSource
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
        super(ApplicationFrame, self).__init__(parent)
        self.setupUi(self)

        # Setup the placeholders
        self.setWindowTitle("BE-BI Application Frame")
        # self.setWindowIcon(QIcon('resources/images/CERN_logo.png'))
        self.central_widget = self.central_widget_container.findChild(QTabWidget, "main_tabs_widget")

        # Our parameter and selector to receive updates from
        parameter_name = "TEST_DEVICE/Acquisition#sin"
        selector = "LHC.USER.ALL"

        # Create the data sources
        timing_source = LocalTimerTimingSource()
        data_source = SinusCurveSource()
        # data_source = SinglePointSource(parameter_name, selector)

        # Setup the plot
        self.scrolling_plot = self.central_widget.findChild(ScrollingPlotWidget, "scrolling_plot")
        self.scrolling_plot.timing_source = timing_source
        self.scrolling_plot.time_span = TimeSpan(10.0, 0.0),
        self.scrolling_plot.time_progress_line = True

        # Connect plot and datasource
        self.scrolling_plot.addCurve(data_source=data_source)

        # Same goes for the CyclicPlot in Tab 2
        self.cyclic_plot = self.central_widget.findChild(CyclicPlotWidget, "cyclic_plot")
        self.cyclic_plot.timing_source = timing_source
        self.cyclic_plot.time_span = TimeSpan(10.0, 0.0),
        self.cyclic_plot.time_progress_line = True
        self.cyclic_plot.addCurve(data_source=data_source)

        # Log something to see it in the LogDisplay Widget
        print(threading.currentThread().getName())
        logging.debug("This message won't be visible, because the default log level is INFO")
        logging.info("This is a message from the application.")

    def setCentralWidget(self, widget):
        self.central_widget = widget
        self.central_widget_container.layout().replaceWidget(self.central_widget, widget)
