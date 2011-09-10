"""
/***************************************************************************
 foss4g2011_example3_starterDialog
                                 A QGIS plugin
 Example #3 starter from FOSS4G 2011 Workshop
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
from ui_foss4g2011_example3_starter import Ui_foss4g2011_example3_starter
# create the dialog for zoom to point
class foss4g2011_example3_starterDialog(QtGui.QDialog, Ui_foss4g2011_example3_starter):
    def __init__(self, iface):
        QtGui.QDialog.__init__(self, iface.mainWindow())
        self.iface = iface
        self.setupUi(self)
