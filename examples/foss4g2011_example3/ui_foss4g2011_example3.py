# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_foss4g2011_example3.ui'
#
# Created: Wed Aug 31 12:10:42 2011
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_foss4g2011_example3(object):
    def setupUi(self, foss4g2011_example3):
        foss4g2011_example3.setObjectName(_fromUtf8("foss4g2011_example3"))
        foss4g2011_example3.resize(862, 576)
        self.gridLayout = QtGui.QGridLayout(foss4g2011_example3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mainWindowVerticalLayout = QtGui.QVBoxLayout()
        self.mainWindowVerticalLayout.setObjectName(_fromUtf8("mainWindowVerticalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widget = QtGui.QWidget(foss4g2011_example3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.addSignalLineEdit = QtGui.QLineEdit(self.widget)
        self.addSignalLineEdit.setObjectName(_fromUtf8("addSignalLineEdit"))
        self.horizontalLayout_3.addWidget(self.addSignalLineEdit)
        self.addSignalButton = QtGui.QPushButton(self.widget)
        self.addSignalButton.setObjectName(_fromUtf8("addSignalButton"))
        self.horizontalLayout_3.addWidget(self.addSignalButton)
        self.verticalLayout_4.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(foss4g2011_example3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.outputTextEdit = QtGui.QTextEdit(self.widget_2)
        self.outputTextEdit.setObjectName(_fromUtf8("outputTextEdit"))
        self.horizontalLayout_4.addWidget(self.outputTextEdit)
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_5.addWidget(self.label)
        self.signalsWeAreListeningToTextEdit = QtGui.QTextEdit(self.widget_3)
        self.signalsWeAreListeningToTextEdit.setObjectName(_fromUtf8("signalsWeAreListeningToTextEdit"))
        self.verticalLayout_5.addWidget(self.signalsWeAreListeningToTextEdit)
        self.horizontalLayout_4.addWidget(self.widget_3)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.mainWindowVerticalLayout.addLayout(self.verticalLayout_4)
        self.okButtonBox = QtGui.QDialogButtonBox(foss4g2011_example3)
        self.okButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.okButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.okButtonBox.setObjectName(_fromUtf8("okButtonBox"))
        self.mainWindowVerticalLayout.addWidget(self.okButtonBox)
        self.gridLayout.addLayout(self.mainWindowVerticalLayout, 0, 0, 1, 1)

        self.retranslateUi(foss4g2011_example3)
        QtCore.QObject.connect(self.okButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), foss4g2011_example3.accept)
        QtCore.QObject.connect(self.okButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), foss4g2011_example3.reject)
        QtCore.QMetaObject.connectSlotsByName(foss4g2011_example3)

    def retranslateUi(self, foss4g2011_example3):
        foss4g2011_example3.setWindowTitle(QtGui.QApplication.translate("foss4g2011_example3", "foss4g2011_example3", None, QtGui.QApplication.UnicodeUTF8))
        self.addSignalButton.setText(QtGui.QApplication.translate("foss4g2011_example3", "Add Signal", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("foss4g2011_example3", "Signals We Are Listening To...", None, QtGui.QApplication.UnicodeUTF8))

