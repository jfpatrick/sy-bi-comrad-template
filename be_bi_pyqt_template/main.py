
import sys
import logging

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox
from be_bi_application_frame.application_frame import ApplicationFrame

from be_bi_pyqt_template.widgets.example_widget import ExampleWidget
from be_bi_pyqt_template.constants import APPLICATION_NAME, AUTHOR, EMAIL


def main():
    logging.info("Starting up {}...".format(APPLICATION_NAME))

    app = QApplication(sys.argv)
    window = ApplicationFrame()

    try:
        example_widget = ExampleWidget(parent=window)
        example_widget.setWindowIcon(QIcon('resources/images/CERN_logo.png'))
        window.setCentralWidget(example_widget)
        window.setWindowTitle(APPLICATION_NAME)

    except Exception as e:
        dialog = QMessageBox()
        dialog.critical(window, "Error", "An Exception occurred at startup:\n\n{}\n\n".format(e) +
                                         "See the logs for more informations, " +
                                         "and please report this issue to {} ({})".format(AUTHOR, EMAIL))
        window.deleteLater()
        return

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
