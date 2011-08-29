# vector_selectbypoint.py code::

    # Import the PyQt and QGIS libraries
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from qgis.core import *
    from qgis.gui import * 
    # Initialize Qt resources from file resources.py
    import resources
    # Import the code for the dialog
    from vector_selectbypointdialog import vector_selectbypointDialog
    import pdb

    class vector_selectbypoint:

        def __init__(self, iface):
            # Save reference to the QGIS interface
            self.iface = iface
            # refernce to map canvas
            self.canvas = self.iface.mapCanvas() 
            # out click tool will emit a QgsPoint on every click
            self.clickTool = QgsMapToolEmitPoint(self.canvas)
            # create our GUI dialog
            self.dlg = vector_selectbypointDialog()
            # create a list to hold our selected feature ids
            self.selectList = []
            # current layer ref (set in handleLayerChange)
            self.cLayer = None
            # current layer dataProvider ref (set in handleLayerChange)
            self.provider = None 

        def initGui(self):
            # Create action that will start plugin configuration
            self.action = QAction(QIcon(":/plugins/vector_selectbypoint/icon.png"), \
                "some text that appears in the menu", self.iface.mainWindow())
            # connect the action to the run method
            QObject.connect(self.action, SIGNAL("triggered()"), self.run)

            # Add toolbar button and menu item
            self.iface.addToolBarIcon(self.action)
            self.iface.addPluginToMenu("&some text that appears in the menu", self.action)

            # connect our custom function to a clickTool signal that the canvas was clicked
            # result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
            #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )
        
            # connect to state change signal of checkbox
            result = QObject.connect(self.dlg.getChkActivate(), SIGNAL("stateChanged(int)"), self.changeActive)

            # connect to the currentLayerChanged signal of QgsInterface
            result = QObject.connect(self.iface, SIGNAL("currentLayerChanged(QgsMapLayer *)"), self.handleLayerChange)
            # QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )


        def unload(self):
            # Remove the plugin menu item and icon
            self.iface.removePluginMenu("&some text that appears in the menu",self.action)
            self.iface.removeToolBarIcon(self.action)

        def handleMouseDown(self, point, button):
            self.dlg.clearTextBrowser()
            self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )
            #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

        def handleLayerChange(self, layer):
            self.cLayer = self.canvas.currentLayer()		
            if self.cLayer:
                self.provider = self.cLayer.dataProvider()

        def updateTextBrowser(self):
            if self.selectList:
                # find the index of the index of the 'NAME' column, branch if has one or not
                nIndx = self.provider.fieldNameIndex('NAME')
                # get our selected feature, but we have to pass in an empty feature and the column index we want
                sFeat = QgsFeature()
                if self.provider.featureAtId(self.selectList[0], sFeat, True, [nIndx]):
                    if nIndx != -1:
                        # get the feature attributeMap
                        attMap = sFeat.attributeMap()
                        # update the TextBrowser
                        self.dlg.clearTextBrowser()
                        # when we first retrieve the value of 'NAME' it comes as a QString so we have to cast it to a Python string
                        self.dlg.setTextBrowser( str( attMap[nIndx].toString() ))
            
                

        def selectFeature(self, point, button):
            # reset selection list on each new selection
            self.selectList = []
            #QMessageBox.information( self.iface.mainWindow(),"Info", "in selectFeature function" )
            # setup the provider select 
            pntGeom = QgsGeometry.fromPoint(point)	
            pntBuff = pntGeom.buffer(2.0,1) #buffer it 2 degrees and return with 1 segment
            rect = pntGeom.boundingBox()
            if self.cLayer:
                feat = QgsFeature()
                # create the select statement
                self.provider.select([],rect) # the arguments mean no attributes returned, and do a bbox filter with our buffered rectangle to limit the amount of features	
                while self.provider.nextFeature(feat):
                    # if the feat geom returned from the selection intersects our point then put it in a list
                    if feat.geometry().intersects(pntGeom):
                        self.selectList.append(feat.id())

                if self.selectList:
                    # make the actual selection	
                    self.cLayer.setSelectedFeatures(self.selectList)
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
                QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)
            

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


