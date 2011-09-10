"""
/***************************************************************************
 foss4g2011_example2Dialog
                                 A QGIS plugin
 Example #2 for FOSS4G 2011 Workshop
                             -------------------
        begin                : 2011-08-31
        copyright            : (C) 2011 by FOSS4G
        email                : info@cugos.org
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
from ui_foss4g2011_example2 import Ui_foss4g2011_example2
# create the dialog for zoom to point
class foss4g2011_example2Dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_foss4g2011_example2()
        self.ui.setupUi(self)

    def clearTextBrowser(self):
        self.ui.txtFeedback.clear() 

    def setTextBrowser(self,value):
        self.ui.txtFeedback.setText(value)



