"""
/***************************************************************************
 rastervaluedisplay
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from rastervaluedisplaydialog import rastervaluedisplayDialog

class rastervaluedisplay:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # map canvas ref
        self.canvas = self.iface.mapCanvas()
        # create and show the dialog
        self.dlg = rastervaluedisplayDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/rastervaluedisplay/icon.png"), \
            "a tool that displays raster values on-the-fly", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&a tool that displays raster values on-the-fly", self.action)
        
        #Add a connection to the xycoord signal of the map canvas
        result = QObject.connect(self.canvas, SIGNAL("xyCoordinates (const QgsPoint &)"), self.handleXY)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&a tool that displays raster values on-the-fly",self.action)
        self.iface.removeToolBarIcon(self.action)

    def handleXY(self, point):
        #QMessageBox.information( self.iface.mainWindow(), "Info", str(point.x()) + "," + str(point.y()) )
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


