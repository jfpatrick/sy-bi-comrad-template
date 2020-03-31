
import sys
import logging

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from be_bi_application_frame.application_frame import ApplicationFrame

from be_bi_pyqt_template.widgets.example_widget import ExampleWidget
from be_bi_pyqt_template.constants import APPLICATION_NAME


def main():
    logging.info("Starting up {}...".format(APPLICATION_NAME))

    app = QApplication(sys.argv)
    window = ApplicationFrame()
    example_widget = ExampleWidget(parent=window)
    window.setCentralWidget(example_widget)

    window.setWindowTitle(APPLICATION_NAME)
    example_widget.setWindowIcon(QIcon('resources/images/CERN_logo.png'))

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
