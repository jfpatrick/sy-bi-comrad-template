from PyQt5 import QtWidgets, QtCore
from pyLogConsole import LogConsole


class ApplicationFrame(QtWidgets.QMainWindow):
    def __init__(self, **kwargs):
        super().__init__()
        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical, self)
        splitter.setOpaqueResize(False)
        splitter.insertWidget(1, LogConsole(parent=splitter, **kwargs))
        super().setCentralWidget(splitter)
        self.splitter = splitter

    def setCentralWidget(self, QWidget):
        self.splitter.insertWidget(0, QWidget)
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 0)
        self.splitter.setCollapsible(1, False)

    def setLayout(self, QLayout):
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(QLayout)
