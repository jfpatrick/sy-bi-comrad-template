import logging
import threading

from PyQt5.QtWidgets import QWidget, QTabWidget, QSpinBox
from PyQt5.QtGui import QIcon

from accwidgets.graph import TimeSpan, ScrollingPlotWidget, CyclicPlotWidget

from be_bi_application_frame.models.data_source import DummyAppModel, DeviceTimingSource, SinglePointSource
from be_bi_application_frame.resources.generated.ui_application_frame import Ui_Form as Ui_ApplicationFrame


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

        # Instantiate the view
        self.setupUi(self)

        # Instantiate the model
        self.model = DummyAppModel()

        # Setup the placeholders
        self.setWindowTitle("BE-BI Application Frame")
        self.setWindowIcon(QIcon('resources/images/CERN_logo.png'))
        self.central_widget = self.central_widget_container.findChild(QTabWidget, "main_tabs_widget")

        # Setup the plots
        scrolling_plot = self.central_widget.findChild(ScrollingPlotWidget, "scrolling_plot")
        self._setup_plot(scrolling_plot, parameter="TEST_DEVICE/Acquisition#sin", selector="LHC.USER.ALL")

        cyclic_plot = self.central_widget.findChild(CyclicPlotWidget, "cyclic_plot")
        self._setup_plot(cyclic_plot, parameter="TEST_DEVICE/Acquisition#cos", selector="LHC.USER.ALL")

        # Setup the control widgets for amplitude and frequency
        amplitude_sin = self.central_widget.findChild(QSpinBox, "amplitude_sin")
        frequency_sin = self.central_widget.findChild(QSpinBox, "frequency_sin")
        amplitude_cos = self.central_widget.findChild(QSpinBox, "amplitude_cos")
        frequency_cos = self.central_widget.findChild(QSpinBox, "frequency_cos")
        amplitude_sin.setValue(self.model.get_amplitude_sin())
        frequency_sin.setValue(self.model.get_frequency_sin())
        amplitude_cos.setValue(self.model.get_amplitude_cos())
        frequency_cos.setValue(self.model.get_frequency_cos())
        amplitude_sin.valueChanged.connect(self.model.set_amplitude_sin)
        frequency_sin.valueChanged.connect(self.model.set_frequency_sin)
        amplitude_cos.valueChanged.connect(self.model.set_amplitude_cos)
        frequency_cos.valueChanged.connect(self.model.set_frequency_cos)

        # Log something to see it in the LogDisplay Widget
        logging.debug("This message won't be visible, because the default log level is INFO")
        logging.info("This is a message from the application.")

    def _setup_plot(self, plot_widget, parameter, selector):
        # Create the data sources
        timing_source = DeviceTimingSource(parameter, selector)
        data_source = SinglePointSource(parameter, selector)

        # Setup the plot
        plot_widget.timing_source = timing_source
        plot_widget.time_span = TimeSpan(10.0, 0.0),
        plot_widget.time_progress_line = True

        # Connect plot and datasource
        plot_widget.addCurve(data_source=data_source)

    def setCentralWidget(self, widget):
        self.central_widget = widget
        self.central_widget_container.layout().replaceWidget(self.central_widget, widget)
