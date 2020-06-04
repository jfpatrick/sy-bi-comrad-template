import logging

from PyQt5.QtWidgets import QTabWidget, QSpinBox

from pyqtgraph import PlotWidget  # For typing
from accwidgets.graph import TimeSpan, ScrollingPlotWidget

# Import the models
from be_bi_pyqt_template.models.data_source import ExampleModel, DeviceTimingSource, SinglePointSource

# Import the code generated from the example_widget.ui file
from be_bi_pyqt_template.resources.generated.ui_example_widget import Ui_TabWidget


class ExampleWidget(QTabWidget, Ui_TabWidget):
    """
    This is the main class defining your GUI. In an MVP perspective,
    this is a Presenter, so a component acting as a proxy between Model
    and View.

    The Model will connect to the control systems or any other source of data,
    and is in the ``models/`` folder. The View is the code generated from
    your ``.ui`` files.

    Qt's signals and slots are usually connected in this class, in the
    ``__init__`` function.
    The model will usually emit signal which are catch either directly
    by the View, or by this class, which translates them into operations
    on the View.

    In this example we are connecting the plots on the View with the ``DataSource``
    classes defined in the ``models/`` folder, and the ``SpinBox`` to the control system
    through the ``ExampleModel`` class, that performs PyJAPC SET operations.
    """

    def __init__(self, parent=None):
        """
        This function creates the Presented. Sets up its View, its Model(s) and connects them together.
        :param parent: None.
        """
        super(ExampleWidget, self).__init__(parent)

        # Instantiate the view
        self.setupUi(self)

        # Instantiate the model
        self.model = ExampleModel()

        # Select the plot from the View
        scrolling_plot = self.findChild(ScrollingPlotWidget, "scrolling_plot")
        # Set it up
        self._setup_plot(scrolling_plot, parameter="BISWRef1/Acquisition#angle", selector="")

        # Select the spinbox from the View
        frequency_scrolling_plot = self.findChild(QSpinBox, "frequency_scrolling_plot")
        # Set the spinbox's initial value
        frequency_scrolling_plot.setValue(self.model.get_frequency())
        # Connect the spinbox to the control system.
        frequency_scrolling_plot.valueChanged.connect(self.model.set_frequency)

        # Log something to see it in the LogDisplay Widget
        logging.debug("This message won't be visible, because the default log level is INFO")
        logging.info("This is a message from the application.")

    @staticmethod
    def _setup_plot(plot_widget: PlotWidget, parameter: str, selector: str) -> None:
        """
        Helper function to show how to setup a plot from accwidgets.
        :param plot_widget: the widget taken from the View
        :param parameter: The Device/Property#field to take data from
        :param selector: The PyJAPC selector to use.
        :return: None.
        """
        # Create the timing source
        timing_source = DeviceTimingSource(parameter, selector)
        # Add the timing source to the plot widget
        plot_widget.timing_source = timing_source

        # Create the actual data source
        data_source = SinglePointSource(parameter, selector)
        # Add it as a curve to the plot
        plot_widget.addCurve(data_source=data_source)

        # Setup the plot's timespan
        plot_widget.time_span = TimeSpan(10.0, 0.0),

        # Show the progress line
        plot_widget.time_progress_line = True
