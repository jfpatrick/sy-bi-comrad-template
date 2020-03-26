
import sys
import logging

from PyQt5.QtWidgets import QApplication

from be_bi_application_frame.application_frame import ApplicationFrame


def main():
    logging.info("Preparing the Application Frame...")
    app = QApplication(sys.argv)
    window = ApplicationFrame()
    # window.setCentralWidget( <your GUI> )
    #   or
    # window.central_widget.removeTab(0)
    # window.central_widget.removeTab(1)
    # window.central_widget.addTab( <first tab of your GUI> )
    # window.central_widget.addTab( <second tab of your GUI> )
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
