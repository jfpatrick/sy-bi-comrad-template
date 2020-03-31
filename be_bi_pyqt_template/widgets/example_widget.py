import logging

from PyQt5.QtWidgets import QTabWidget, QSpinBox
from accwidgets.graph import TimeSpan, ScrollingPlotWidget, CyclicPlotWidget

# Import the models
from be_bi_pyqt_template.models.data_source import ExampleModel, DeviceTimingSource, SinglePointSource
# Import the code generated from the example_widget.ui file
from be_bi_pyqt_template.resources.generated.ui_example_widget import Ui_TabWidget


class ExampleWidget(QTabWidget, Ui_TabWidget):
    """
        This is the main class defining your GUI. In an MVP perspective,
        this is a Presenter, so a component acting as a proxy between Model
        and View.

        The Model will connect to the control systems or any other source of data.
        The View is the code generated from your *.ui files.

        Signals and slots are usually connected in this class, in the init.
        The model will usually emit signal which are catched either directly
        by the View, or by this class, which translates them into operations
        on the View.
    """
    def __init__(self, parent=None):
        super(ExampleWidget, self).__init__(parent)

        # Instantiate the view
        self.setupUi(self)

        # Instantiate the model
        self.model = ExampleModel()

        # Setup the plots
        scrolling_plot = self.findChild(ScrollingPlotWidget, "scrolling_plot")
        self._setup_plot(scrolling_plot, parameter="TEST_DEVICE/Acquisition#sin", selector="LHC.USER.ALL")

        cyclic_plot = self.findChild(CyclicPlotWidget, "cyclic_plot")
        self._setup_plot(cyclic_plot, parameter="TEST_DEVICE/Acquisition#cos", selector="LHC.USER.ALL")

        # Setup the control widgets for amplitude and period
        amplitude_sin = self.findChild(QSpinBox, "amplitude_sin")
        period_sin = self.findChild(QSpinBox, "period_sin")
        amplitude_cos = self.findChild(QSpinBox, "amplitude_cos")
        period_cos = self.findChild(QSpinBox, "period_cos")
        amplitude_sin.setValue(self.model.get_amplitude_sin())
        period_sin.setValue(self.model.get_period_sin())
        amplitude_cos.setValue(self.model.get_amplitude_cos())
        period_cos.setValue(self.model.get_period_cos())
        amplitude_sin.valueChanged.connect(self.model.set_amplitude_sin)
        period_sin.valueChanged.connect(self.model.set_period_sin)
        amplitude_cos.valueChanged.connect(self.model.set_amplitude_cos)
        period_cos.valueChanged.connect(self.model.set_period_cos)

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
