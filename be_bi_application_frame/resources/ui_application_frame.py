# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sps_bgi_expert_gui/resources/application_frame.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1606, 1101)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("padding: 10px;border:1px solid #aaaaaa;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(1137, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("padding: 10px;margin:10px;")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.central_widget_container = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget_container.sizePolicy().hasHeightForWidth())
        self.central_widget_container.setSizePolicy(sizePolicy)
        self.central_widget_container.setObjectName("central_widget_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central_widget_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.placeholder = QtWidgets.QLabel(self.central_widget_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder.sizePolicy().hasHeightForWidth())
        self.placeholder.setSizePolicy(sizePolicy)
        self.placeholder.setMinimumSize(QtCore.QSize(0, 400))
        font = QtGui.QFont()
        font.setItalic(True)
        self.placeholder.setFont(font)
        self.placeholder.setStyleSheet("color: gray; background-color: #ccc;")
        self.placeholder.setAlignment(QtCore.Qt.AlignCenter)
        self.placeholder.setObjectName("placeholder")
        self.verticalLayout_2.addWidget(self.placeholder)
        self.CLogDisplay = CLogDisplay(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CLogDisplay.sizePolicy().hasHeightForWidth())
        self.CLogDisplay.setSizePolicy(sizePolicy)
        self.CLogDisplay.setProperty("logLevel", PyDMLogDisplay.INFO)
        self.CLogDisplay.setObjectName("CLogDisplay")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Future location of the Timing Display"))
        self.pushButton.setText(_translate("Form", "RBAC Token"))
        self.placeholder.setText(_translate("Form", "Your widgets go here"))
        self.CLogDisplay.setProperty("logFormat", _translate("Form", "%(asctime)s %(message)s"))
from comrad.widgets.tables import CLogDisplay
from pydm.widgets.logdisplay import PyDMLogDisplay
