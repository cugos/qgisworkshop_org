"""
/***************************************************************************
 rastervaluedisplayDialog
                                 A QGIS plugin
 a tool that displays raster values on-the-fly
                             -------------------
        begin                : 2011-08-25
        copyright            : (C) 2011 by CUGOS
        email                : none@cugos.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_rastervaluedisplay import Ui_rastervaluedisplay
# create the dialog for zoom to point
class rastervaluedisplayDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_rastervaluedisplay()
        self.ui.setupUi(self)

    def clearTextBrowser(self):
        self.ui.txtFeedback.clear() 

    def setTextBrowser(self,value):
        self.ui.txtFeedback.setText(value)
