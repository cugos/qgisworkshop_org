
=========================================================
Handout: Take Home Points
=========================================================

Accessing Layers through QgisInterface and QgsMapCanvas 
----------------------------------------------------------

Using QgisInteface.activeLayer()
***************************************

Return a reference to the selected layer in the table of contents::

    >>> aLayer = qgis.utils.iface.activeLayer()
    >>> aLayer
    <qgis.core.QgsRasterLayer object at 0x99ea6ec>
    >>> aLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

Using QgsMapCanvas.currentLayer()
***************************************

Another common way of accessing the selected layer in the table of contents is to get at it using the\  `QgsMapCanvas <http://doc.qgis.org/head/classQgsMapCanvas.html>`_ \like so::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> cLayer = canvas.currentLayer()
    >>> cLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

Getting all visible layers QgsMapCanvas.layers()
********************************************************

With the map canvas class we can get more than just the active layer -- we can get all visible layers (those that are turned on in the TOC)::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> allLayers = canvas.layers()
    >>> for i in allLayers: print i.name()
    ... 
    50m_populated_places_simple

Getting layers by index using QgsMapCanvas.layer()
**********************************************************

Layers are stacked top-down and accessed through a zero-based index. That means the first layer (topmost layer) starts at index 0. We pass in a integer designating the index we want::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> canvas.layer(0)
    <qgis.core.QgsVectorLayer object at 0x99eaeec>
    >>> canvas.layer(0).name()
    PyQt4.QtCore.QString(u'50m_populated_places_simple') 

----------------------------------

Accessing Features (Attributes and Geometry)
----------------------------------------------------------

Using QgsVectorDataProvider.select()
****************************************

Loop through all layer features::

    # using the 50m_admin_0_countries.shp from natural earth download for this example
    cLayer = qgis.utils.iface.mapCanvas().currentLayer()
    provider = cLayer.dataProvider()
    columnList = []
    for i in ['NAME']:
        columnList.append(provider.fieldNameIndex(i))

    rect = QgsRectangle(QgsPoint(0,0),QgsPoint(20, 34))
    provider.select(selectList, rect, True, False)
    feat = QgsFeature()
    while provider.nextFeature(feat):
        att = feat.attributeMap()
        for key, value in att.items(): print str(value.toString())

Using QgsVectorDataProvider.featureAtId()
********************************************

If we have the feature IDs that we want, then we don't need to loop through all features::

    # using the 50m_admin_0_countries.shp from natural earth download for this example
    cLayer = qgis.utils.iface.mapCanvas().currentLayer()
    provider = cLayer.dataProvider()
    selectList = [ 24, 32, 45, 56 ]
    if selectList:
        for id in selectList:
            nIndx = provider.fieldNameIndex('NAME')
            sFeat = QgsFeature()
            if provider.featureAtId(id, sFeat, True, [nIndx]):
                if nIndx != -1:
                    attMap = sFeat.attributeMap()
                    print str( attMap[nIndx].toString() )

------------------------------------

SIGNAL and SLOT Examples
----------------------------

Emit a Signal
****************

Using the\  ``QgsMapCanvas`` \object as an example. Here is how we emit a signal::

    self.iface.mapCanvas().emit(SIGNAL("xyCoordinates(const QgsPoint &)"), QgsPoint(-122,45))

Connect Slot to Signal
***************************

Here we connect custom slot function\  ``listen_xyCoordinates`` \to the\  ``"xyCoordinates(const QgsPoint &)"`` \signal::

    # the connection
    QObject.connect(self.iface.mapCanvas(), SIGNAL("xyCoordinates(const QgsPoint &)"), self.listen_xyCoordinates)

    # the custome slot function
    def listen_xyCoordinates(self,point):
        self.dlg.outputTextEdit.append("xyCoordinates - %d,%d" % (point.x() if point else "",point.y() if point else ""))

------------------------------------

Debugging with Pdb
------------------------------

The PyQT debug hook
*********************

Make sure you import pdb before you try to use it::
    
    import pdb

You will need to add the\  ``pdb.set_trace()`` \where you would like to set a break point in your code::

    pyqtRemoveInputHook()
    pdb.set_trace()

Start QGIS from the command prompt and you'll be dropped into a PDB prompt where you can run pdb commands and normal Python statements. Here's a brief list of pdb commands. See the\  `official pdb docs <http://docs.python.org/library/pdb.html>`_ \for more examples:

    ``list # list source code with currently executing line in the middle``

    ``list <line number> # list source code with <line number> argument in the middle``

    ``list <line number from> , <line number to> # list source code between <line number> arguments``
    
    ``break # break with NO args returns all the breakpoints (and break IDs) you have in your debug code``

    ``break <line number> # create a new break point in the code at the <line number> argument``

    ``next # move through code execution one line at a time. Running next on function call steps over (not into) function execution``
    
    ``step # move through code execution one line at a time. Running step on function call steps into (not over) function execution``
    
    ``cl <breakpoint ID> # remove a break identified by it's <breakpoint ID>``

-----------------------------

Creating a Plugin Repository
-------------------------------

If you want to fetch your plugins through QGIS then you need to create a web-accessible XML file that tells QGIS where to download the plugin::

    <?xml version = '1.0' encoding = 'UTF-8'?>
    <?xml-stylesheet type='text/xsl' href='/plugins.xsl' ?>
    <plugins>
      <pyqgis_plugin name='Plugin Installer' version='1.1'>
        <description>The recent Python Plugin Installer</description>
        <version>1.1</version>
        <qgis_minimum_version>1.0</qgis_minimum_version>
        <homepage>http://www.bwj.aster.net.pl/qgis/</homepage>
        <file_name>plugin_installer.zip</file_name>
        <author_name>Borys Jurgiel</author_name>
        <download_url>http://spatialserver.net/pyqgis_1.0/plugins/plugin_installer.zip</download_url>
        <uploaded_by>borysiasty</uploaded_by>
        <create_date>2008-12-18</create_date>
        <update_date>2010-10-31</update_date>
      </pyqgis_plugin>
    </plugins>


