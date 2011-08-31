"""
/***************************************************************************
 foss4g2011_example2
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from foss4g2011_example2dialog import foss4g2011_example2Dialog

class foss4g2011_example2:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # map canvas ref
        self.canvas = self.iface.mapCanvas()
        # create and show the dialog
        self.dlg = foss4g2011_example2Dialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/foss4g2011_example2/icon.png"), \
            "Example #2 for FOSS4G 2011 Workshop", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Example #2 for FOSS4G 2011 Workshop", self.action)
        
        #Add a connection to the xycoord signal of the map canvas
        result = QObject.connect(self.canvas, SIGNAL("xyCoordinates (const QgsPoint &)"), self.handleXY)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Example #2 for FOSS4G 2011 Workshop",self.action)
        self.iface.removeToolBarIcon(self.action)

    def handleXY(self, point):
        self.dlg.clearTextBrowser()
        self.cLayer = self.canvas.currentLayer()
        if self.cLayer:
            if self.cLayer.type() == 1:
                success, data = self.cLayer.identify(point)
                final = "" 
                for key,value in data.items():
                    final += str(key) + " > " + str(value) + "\n"
                self.dlg.setTextBrowser(final) 

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass

