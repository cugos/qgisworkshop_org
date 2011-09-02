"""
/***************************************************************************
 foss4g2011_example1
                                 A QGIS plugin
 Example #1 for FOSS4G 2011 Workshop
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
from foss4g2011_example1dialog import foss4g2011_example1Dialog

class foss4g2011_example1:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # refernce to map canvas
        self.canvas = self.iface.mapCanvas() 
        # the identify tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # create our GUI dialog
        self.dlg = foss4g2011_example1Dialog()
        # create a list to hold our selected feature ids
        self.selectList = []
        # current layer ref (set in handleLayerChange)
        self.cLayer = None
        # current layer dataProvider ref (set in handleLayerChange)
        self.provider = None 

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/foss4g2011_example1/icon.png"), \
            "Example #1 for FOSS4G 2011 Workshop", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Example #1 for FOSS4G 2011 Workshop", self.action)

        # connect to the currentLayerChanged signal of QgsInterface
        result = QObject.connect(self.iface, SIGNAL("currentLayerChanged(QgsMapLayer *)"), self.handleLayerChange)

        # connect to the selectFature custom function to the map canvas click event        
        QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)


    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("Example #1 for FOSS4G 2011 Workshop",self.action)
        self.iface.removeToolBarIcon(self.action)


    def handleMouseDown(self, point, button):
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )

    def handleLayerChange(self, layer):
        self.cLayer = self.canvas.currentLayer()        
        if self.cLayer:
            self.provider = self.cLayer.dataProvider()

    def updateTextBrowser(self):
        # check to make sure we have a feature selected in our selectList -- note that there might be more than one feature
        if self.selectList:

            # ############ EXAMPLE 1 EDITS GO HERE ####################  
            ''' write code that will output ALL selected feature attributes for a single feature into the Text Browser''' 
            ''' instead of using the dataProvider.select() function get the actual QgsFeature using dataProvider.featureAtId() '''

            self.dlg.setTextBrowser("example text\nto populate TextBrowser")
            

    def selectFeature(self, point, button):
        # reset selection list on each new selection
        self.selectList = []
        pntGeom = QgsGeometry.fromPoint(point)  
        pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 2),0) 
        rect = pntBuff.boundingBox()
        if self.cLayer:
            feat = QgsFeature()
            # create the select statement
            self.provider.select([],rect) # the arguments mean no attributes returned, and do a bbox filter with our buffered rectangle to limit the amount of features 
            while self.provider.nextFeature(feat):
                # if the feat geom returned from the selection intersects our point then put it in a list
                if feat.geometry().intersects(pntBuff):
                    self.selectList.append(feat.id())

            if self.selectList:
                # make the actual selection 
                self.cLayer.setSelectedFeatures([self.selectList[0]])
                # update the TextBrowser
                self.updateTextBrowser()
        else:   
                QMessageBox.information( self.iface.mainWindow(),"Info", "No layer currently selected in TOC" )


    # run method that performs all the real work
    def run(self):
        # set the current layer immediately if it exists, otherwise it will be set on user selection
        self.cLayer = self.iface.mapCanvas().currentLayer()
        if self.cLayer: self.provider = self.cLayer.dataProvider()

        # make identify the tool we'll use 
        self.canvas.setMapTool(self.clickTool) 

        # show the dialog
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass

