# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_foss4g2011_example3.ui'
#
# Created: Wed Aug 31 11:07:45 2011
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
        foss4g2011_example3.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(foss4g2011_example3)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(foss4g2011_example3)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), foss4g2011_example3.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), foss4g2011_example3.reject)
        QtCore.QMetaObject.connectSlotsByName(foss4g2011_example3)

    def retranslateUi(self, foss4g2011_example3):
        foss4g2011_example3.setWindowTitle(QtGui.QApplication.translate("foss4g2011_example3", "foss4g2011_example3", None, QtGui.QApplication.UnicodeUTF8))

