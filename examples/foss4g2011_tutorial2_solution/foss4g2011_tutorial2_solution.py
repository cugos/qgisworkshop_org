"""
/***************************************************************************
 foss4g2011_tutorial2_solution
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import * 
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from foss4g2011_tutorial2_solutiondialog import foss4g2011_tutorial2_solutionDialog

class foss4g2011_tutorial2_solution:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # reference to map canvas
        self.canvas = self.iface.mapCanvas() 
        # out click tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # create our GUI dialog
        self.dlg = foss4g2011_tutorial2_solutionDialog()
        # create a list to hold our selected feature ids
        self.selectList = []
        # current layer ref (set in handleLayerChange)
        self.cLayer = None
        # current layer dataProvider ref (set in handleLayerChange)
        self.provider = None 

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/foss4g2011_tutorial2_solution/icon.png"), \
            "Tutorial #2 solution for FOSS4G 2011 Workshop", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Tutorial #2 solution for FOSS4G 2011 Workshop", self.action) 

        # connect to stateChanged signal of checkbox
        result = QObject.connect(self.dlg.getChkActivate(), SIGNAL("stateChanged(int)"), self.changeActive)

        # connect to the currentLayerChanged signal of QgsInterface
        result = QObject.connect(self.iface, SIGNAL("currentLayerChanged(QgsMapLayer *)"), self.handleLayerChange)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Tutorial #2 solution for FOSS4G 2011 Workshop",self.action)
        self.iface.removeToolBarIcon(self.action)

    def handleMouseDown(self, point, button):
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )

    def handleLayerChange(self, layer):
        self.cLayer = self.canvas.currentLayer()        
        if self.cLayer:
            self.provider = self.cLayer.dataProvider()

    def updateTextBrowser(self):
        # only if we have something selected
        if self.selectList:
            # find the index of the 'NAME' column if one exists
            nIndx = self.provider.fieldNameIndex('NAME')
            sFeat = QgsFeature()
            # pass in an empty QgsFeature and our feature ids to get the feature we are targetting
            if self.provider.featureAtId(self.selectList[0], sFeat, True, [nIndx]):
                # only if a 'NAME' column exists
                if nIndx != -1:
                    # get the feature attributeMap
                    attMap = sFeat.attributeMap()
                    # clear the TextBrowser
                    self.dlg.clearTextBrowser()
                    # when we first retrieve the value of 'NAME' it comes as a QString so we have to cast it to a Python string
                    self.dlg.setTextBrowser( str( attMap[nIndx].toString() ))
        
            

    def selectFeature(self, point, button):
        # reset selection list on each new selection
        self.selectList = []
        # setup the provider select to filter results based on a rectangle
        pntGeom = QgsGeometry.fromPoint(point)  
        # scale-dependent buffer of 2 pixels-worth of map units
        pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 2),0) 
        rect = pntBuff.boundingBox()
        if self.cLayer:
            feat = QgsFeature()
            # create the select statement
            self.provider.select([],rect) # the arguments mean no attributes returned, and do a bbox filter with our buffered rectangle to limit the amount of features
            while self.provider.nextFeature(feat):
                # if the feat geom returned from the selection intersects our buffered point then put it in a list
                if feat.geometry().intersects(pntBuff):
                    self.selectList.append(feat.id())

            if self.selectList:
                # make the actual selection, only pass one feature b/c more than one might be selected
                self.cLayer.setSelectedFeatures( [self.selectList[0]] )
                # update the TextBrowser
                self.updateTextBrowser()
        else:   
                QMessageBox.information( self.iface.mainWindow(),"Info", "No layer currently selected in TOC" )


    def changeActive(self,state):
        if (state==Qt.Checked):
            # connect to click signal
            # QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
            # connect our select function to the canvasClicked signal
            QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
        else:
            # disconnect from click signal
            # QObject.disconnect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
            # disconnect our select function to the canvasClicked signal
            QObject.disconnect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
        

    # run method that performs all the real work
    def run(self):
        # set the current layer immediately if it exists, otherwise it will be set on user selection
        self.cLayer = self.iface.mapCanvas().currentLayer()
        if self.cLayer: self.provider = self.cLayer.dataProvider()
        # make our clickTool the tool that we'll use for now 
        self.canvas.setMapTool(self.clickTool) 

        # show the dialog
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass

