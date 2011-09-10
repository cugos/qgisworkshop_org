"""
/***************************************************************************
 foss4g2011_tutorial2_solutionDialog
                                 A QGIS plugin
 Tutorial #2 solution for FOSS4G 2011 Workshop
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
from ui_foss4g2011_tutorial2_solution import Ui_foss4g2011_tutorial2_solution
# create the dialog for zoom to point
class foss4g2011_tutorial2_solutionDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_foss4g2011_tutorial2_solution()
        self.ui.setupUi(self)

    def setTextBrowser(self, output):
        self.ui.txtFeedback.setText(output)

    def clearTextBrowser(self):
        self.ui.txtFeedback.clear()

    def getChkActivate(self):
        return self.ui.chkActive

