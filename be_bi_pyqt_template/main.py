import os
import sys
import logging
import pyqt5ac
# Generate the code from .ui and .qrc files in case they are missing or outdated
pyqt5ac.main(config=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pyqt5ac.yml'))

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox
from be_bi_application_frame.application_frame import ApplicationFrame

# Import the Presenter from the widgets folder
from be_bi_pyqt_template.widgets.example_widget import ExampleWidget
from be_bi_pyqt_template.constants import APPLICATION_NAME, AUTHOR, EMAIL


def main():
    """
        Application's entry point. It instantiates the QApplication, the main window
        and the ApplicationFrame widgets, that will contain your GUI.
        Then loads your widgets into the main windows and shows it, entering the event loop.
    """
    logging.info("Starting up {}...".format(APPLICATION_NAME))

    # Instantiate the QApplication and the ApplicationFrame
    app = QApplication(sys.argv)
    window = ApplicationFrame()

    try:
        # Instantiate your GUI (here the ExampleWidget class)
        example_widget = ExampleWidget(parent=window)

        # Apply small customizations to the application (window title, window icon...)
        example_widget.setWindowIcon(QIcon('resources/images/CERN_logo.png'))
        window.setCentralWidget(example_widget)
        window.setWindowTitle(APPLICATION_NAME)

    except Exception as e:

        # If something goes wrong, shows a small QDialog with an error message and quits
        dialog = QMessageBox()
        dialog.critical(window, "Error", "An Exception occurred at startup:\n\n{}\n\n".format(e) +
                                         "See the logs for more information, " +
                                         "and please report this issue to {} ({})".format(AUTHOR, EMAIL))
        window.deleteLater()
        return

    # Enter the event loop by showing the window
    window.show()

    # Once left the event loop, terminates the application
    sys.exit(app.exec_())
