"""
For reference, see:
https://acc-py.web.cern.ch/gitlab/bisw-python/pyqt-tutorial/docs/stable/2-project-structure.html#project-name-widgets
https://acc-py.web.cern.ch/gitlab/bisw-python/pyqt-tutorial/docs/stable/2-project-structure.html#project-name-widgets-resources
"""
from logging import getLogger
from PyQt5.QtWidgets import QTabWidget

# Import the models
from sy_bi_pyqt_template.models.models import SpinBoxModel, SinglePointSource

# Import the code generated from the main_widget.ui file
from sy_bi_pyqt_template.widgets.resources.generated.ui_main_widget import Ui_TabWidget


class MainWidget(QTabWidget, Ui_TabWidget):
    """
    This is the main class defining your GUI. In the ModelView architecture, this is the View.

    It loads the GUI definition from Ui_TabWidget (generated code from the main_widget.ui file)

    Qt's signals and slots are usually connected in this class, in the ``__init__`` function.
    The model will usually emit signal which are catch by this class, which translates them into operations
    on the GUI.

    In this example we are connecting the plots on the View with the ``UpdateSource`` classes defined in the `
    `models/`` folder, and the ``SpinBox`` to the control system through the ``SpinBoxModel`` class, that
    performs PyJAPC SET operations.
    """

    def __init__(self, parent=None):
        """
        This function sets up its View, its Model(s) and connects them together.
        :param parent: the owner of this widget. Should be an ApplicationFrame instance. See the Qt Documentation.
        """
        super(MainWidget, self).__init__(parent)

        # Setup itself as the view
        self.setupUi(self)

        # Instantiate the model
        self.model = SpinBoxModel()

        # Set the spinbox's initial value
        self.frequency_spinbox.setValue(self.model.get_frequency())
        # Connect the spinbox to the control system
        self.frequency_spinbox.valueChanged.connect(self.model.set_frequency)

        # Create the data source model for the plot
        data_source = SinglePointSource(parameter_name="BISWRef1/Acquisition#angle", selector="")
        # Add it as a curve to the plot
        self.scrolling_plot.addCurve(data_source=data_source)

        # Log something to see it in the log widget
        self.logger = getLogger('main')
        self.logger.debug("This message won't be visible, because the default log level is WARNING")
        self.logger.warning("This is a message from the application.")


