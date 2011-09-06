# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_foss4g2011_example1.ui'
#
# Created: Wed Aug 31 14:20:35 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_foss4g2011_example1(object):
    def setupUi(self, foss4g2011_example1):
        foss4g2011_example1.setObjectName("foss4g2011_example1")
        foss4g2011_example1.resize(461, 514)
        self.buttonBox = QtGui.QDialogButtonBox(foss4g2011_example1)
        self.buttonBox.setGeometry(QtCore.QRect(-30, 470, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.txtFeedback = QtGui.QTextBrowser(foss4g2011_example1)
        self.txtFeedback.setGeometry(QtCore.QRect(10, 20, 441, 441))
        self.txtFeedback.setObjectName("txtFeedback")

        self.retranslateUi(foss4g2011_example1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), foss4g2011_example1.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), foss4g2011_example1.reject)
        QtCore.QMetaObject.connectSlotsByName(foss4g2011_example1)

    def retranslateUi(self, foss4g2011_example1):
        foss4g2011_example1.setWindowTitle(QtGui.QApplication.translate("foss4g2011_example1", "foss4g2011_example1", None, QtGui.QApplication.UnicodeUTF8))

