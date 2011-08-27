# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rastervaluedisplay.ui'
#
# Created: Fri Aug 26 16:20:14 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_rastervaluedisplay(object):
    def setupUi(self, rastervaluedisplay):
        rastervaluedisplay.setObjectName("rastervaluedisplay")
        rastervaluedisplay.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(rastervaluedisplay)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.txtFeedback = QtGui.QTextBrowser(rastervaluedisplay)
        self.txtFeedback.setGeometry(QtCore.QRect(50, 10, 256, 192))
        self.txtFeedback.setObjectName("txtFeedback")

        self.retranslateUi(rastervaluedisplay)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), rastervaluedisplay.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), rastervaluedisplay.reject)
        QtCore.QMetaObject.connectSlotsByName(rastervaluedisplay)

    def retranslateUi(self, rastervaluedisplay):
        rastervaluedisplay.setWindowTitle(QtGui.QApplication.translate("rastervaluedisplay", "rastervaluedisplay", None, QtGui.QApplication.UnicodeUTF8))

