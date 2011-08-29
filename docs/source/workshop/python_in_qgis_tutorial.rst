==============================================
Tutorial -- PyQGIS
==============================================


Setup
-------------

\  **1.** \To begin open up a new QGIS session by clicking the QGIS icon on the top menu bar.

    All the data we will be using is located in the\  ``natural_earth_50m`` \directory of your qgis user home path::

    /home/qgis/natural_earth_50m

\  **2.** \Add the following vector and raster files to QGIS::

    /home/qgis/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif
    
    # turn off the tif layer so it doesn't slow things down

    /home/qgis/natural_earth_50m/cultural/50m_cultural/50m_populated_places_simple.shp

\  **3.** \Now open the Python Console by selecting::

    Plugins > Python Console

.. image:: ../_static/python_console.png
    :scale: 100%
    :align: center

------------------------------------------------------

Accessing Layers
--------------------------

.. note:: The hyperlinks that follow all reference the\  `QGIS API documentation <http://doc.qgis.org>`_ \. Click on them to view the classes and methods we are referencing below

There's a number of ways to access the layers in QGIS. Each way starts by first referencing the\  `QgisInterface class <http://doc.qgis.org/head/classQgisInterface.html>`_ \which is called\  **iface** \in the Python bindings.

From the Python Console we access\  **iface** \by calling the following command::
    
    >>> qgis.utils.iface

Type the above command into the Python Console and you should see this output::

    >>> qgis.utils.iface
    <qgis.gui.QgisInterface object at 0x925266c>

Running the above command prints out the actual name of the QGIS class we are dealing with -- indeed iface is the QgisInterface object 

Method 1
*********

On the iface class is a useful function called\  `activeLayer() <http://doc.qgis.org/head/classQgisInterface.html#231f32fbf95004aebb067cb98f3a391c>`_ \that returns us a reference to the selected layer in the table of contents.

\  **1.** \Run the following command::

    >>> aLayer = qgis.utils.iface.activeLayer()
    >>> aLayer
    <qgis.core.QgsRasterLayer object at 0x99ea6ec>

Depending on which layer is selected in the table of contents you will see either a raster or vector layer output. I had the raster layer selected it seems.

\  **2.** \What is the name of the active layer?::

    >>> aLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

\  **3.** \How do you get an idea about what functions this Python object has available? There's really two ways:

    \1) The more visually appealing way to browse class attributes is to access the\  `QGIS API documentation <http://doc.qgis.org>`_ \and search for the class you're working with.

    \2) The Pythonic way (though less visually appealing) is to run the following command on an object you want to know more about::
        
            >>> help(aLayer) 

             # output truncated for demonstration
             ...
             |  extent = <built-in function extent>
             |  
             |  getLayerID = <built-in function getLayerID>
             |  
             |  getTransparency = <built-in function getTransparency>
             ...
             # output truncated for demonstration

The pile of text printed out in the shell is hard to navigate. Above is an example of some of the attributes you might see. It's probably better to use the API link above.

Method 2
**********

\  **1.** \Another common way of accessing the selected layer in the table of contents is to get at it using the\  `QgsMapCanvas <http://doc.qgis.org/head/classQgsMapCanvas.html>`_ \. The mapCanvas class has tons of useful functions::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> cLayer = canvas.currentLayer()
    >>> cLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

Method 3
**********
\  **1.** \With the map canvas class we can get more than just the active layer -- we can get everthing::

    >>> allLayers = canvas.layers()
    >>> for i in allLayers: print i.name()
    ... 
    50m_populated_places_simple

**Wait a minute!** \we have two layers in the table of contents. Why did we only get one single name back? (this outcome assumes that you followed directions and kept the raster layer turned off. If you did not turn off the raster layer then you will see both layer names printed out)

It turns out that using\  ``QgsMapCanvas.layers()`` \will only return us\  **visible** \layers (those that are checked visible).

\  **2.** \Turn on the raster layer in the table of contents. Rerun the exact same two lines of code above::

    >>> allLayers = canvas.layers()
    >>> for i in allLayers: print i.name()
    ... 
    50m_populated_places_simple
    SR_50M

Now we should see both layer names printed out.

Method 4
**********

It's also useful sometimes to access layers in the order they are stacked in the table of contents.

Layers are stacked top-down and accessed through a zero-based index. That means the first layer (topmost layer) starts at index 0.

\  **1.** \We access layers using the\  `QgsMapCanvas.layer() function <http://doc.qgis.org/head/classQgsMapCanvas.html#de2251f2227bc0f0efefd09810a193cd>`_ \and pass in a integer designating the index we want::

    >>> canvas.layer(0)
    <qgis.core.QgsVectorLayer object at 0x99eaeec>
    >>> canvas.layer(0).name()
    PyQt4.QtCore.QString(u'50m_populated_places_simple')    


Other Excercises
********************

- set the active layer using\  `qgis.utils.iface.setActiveLayer() <http://doc.qgis.org/head/classQgisInterface.html#c42281407013002b56ff7ed422c77336>`_

- set the current layer using\  `qgis.utils.iface.mapCanvas().setCurrentLayer() <http://doc.qgis.org/head/classQgsMapCanvas.html#001c20fe97f844542895e718ee166926>`_ 

- can you find the QgsMapLayer class in the documentation and find out how to get a layer's extent?

.. note:: There's probably many more ways to access the layers in the QGIS table of contents...so keep your eyes open for other methods

------------------------------------------------------

Loading Layers into QGIS
-----------------------------

Maybe when you were looking at the QgisInterface class you noticed a couple addLayer methods? Let's use these to load layers into QGIS. 

\  **1.** \Start by turning off all layers currenlty in QGIS by unchecking them. Then with a blank map, re-add the SR_50M and populated places data as a different name::

    >>> qgis.utils.iface.addVectorLayer("/home/qgis/natural_earth_50m/cultural/50m_cultural/50m_populated_places_simple.shp", "pop2", "ogr")
    <qgis.core.QgsVectorLayer object at 0xca0feac>
    >>> qgis.utils.iface.addRasterLayer("/home/qgis/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif", "raster")
    <qgis.core.QgsRasterLayer object at 0xca0fe6c>

The method\  `addVectorLayer <http://doc.qgis.org/head/classQgisInterface.html#39be50fe9974de17177861ad89e7f36e>`_ \takes three arguments:

    - the first argument is the path to the data source -- the shapefile in our case

    - the second argument is the basename -- the name that the layer takes in the table of contents

    - the third argument is the provider key. Basically, the function wants to know what driver will be used to read this data. For our purposes, "ogr" will be used most of the time with vector data 

Notice that the\  `addRasterLayer <http://doc.qgis.org/head/classQgisInterface.html#808a34b507a8c4204d607a5857d62748>`_ \only takes two arguments -- the path and basename for the layer. 

If you go look at the\  **addRasterLayer** \function definition in the link above you'll notice that there are two overloaded function definitions for adding rasters. One definition takes two arguments (the one we used). The other definition takes many more arguments.

Adding a PostGIS Layer
***********************

You might be wondering how you handle adding data that exists in PostGIS. Luckily for you, we have PostGIS setup on the virtual machine with some vector layers already loaded.

Accessing PostGIS vector data uses the same function as we did above --\  `addVectorLayer <http://doc.qgis.org/head/classQgisInterface.html#39be50fe9974de17177861ad89e7f36e>`_ \. However, specifying the path is a little different. 

QGIS supports the idea of uniform resource identifiers (URIs) as data-source descriptions for handling input from databases, CSVs and GPX files. The URI we pass to the database includes such parameters as the database name, username, password and the port it runs on (among other parameters).

\  **1.** \Let's load country polygons from PostgreSQL::

    >>> uri = QgsDataSourceURI()
    >>> uri.setConnection("localhost", "5432", "qgis_workshop", "qgis", "qgis")
    >>> uri.setDataSource("public", "countries", "the_geom")
    >>> uri.uri()
    PyQt4.QtCore.QString(u'dbname=\'qgis_workshop\' host=localhost port=5432 user=\'qgis\' password=\'qgis\' table="public"."countries" (the_geom) sql=')
    >>> qgis.utils.iface.addVectorLayer(uri.uri(), "all_these_countries", "postgres")
    <qgis.core.QgsVectorLayer object at 0xca0feac>

You should now have the countries layer in QGIS

.. image:: ../_static/postgres_countries_layer.png
    :scale: 43%
    :align: center

------------------------------------------------------

Accessing Vector Geometry 
-------------------------------------------------------------

Now it's time for the really fun stuff -- playing with geometry.

The class\  `QgsGeometry <http://doc.qgis.org/head/classQgsGeometry.html>`_ \is one of the most important to study in the QGIS API. It contains the basic spatial predicates and operations for vector data that we are all used to.

For example, with the reference to the geometry of an object we can access these spatial operations (these are only some):
    - buffer
    - intersection
    - combine
    - difference 

Vector Layer Geometry
********************************************

There's a number of ways to access layer features and an individual feature geometry. We will\  **NOT** \walk through all of them here. 

Method 1
**********

One way to access a layer's features is through the\  `QgsVectorDataProvider <http://doc.qgis.org/head/classQgsVectorDataProvider.html>`_ \class. You can get a reference to a data provider directly from your\  `QgsVectorLayer <http://doc.qgis.org/head/classQgsVectorLayer.html>`_ \class.

\  **1.** \First, remove all layers from QGIS


\  **2.** \Then add the layer called\  ``50m_admin_0_countries.shp`` \located here::

    /home/qgis/natural_earth_50m/cultural/50m_cultural/50m_admin_0_countries.shp

\  **3.** \Make sure the Python Console is open. Now get a reference to a the current layer::

    >>> cLayer = qgis.utils.iface.mapCanvas().currentLayer()
    >>> cLayer.name()
    PyQt4.QtCore.QString(u'50m_admin_0_countries')

\  **4.** \Get a reference to the data provider::

    >>> provider = cLayer.dataProvider()
    >>> provider.name()
    PyQt4.QtCore.QString(u'ogr')

If this was a vector layer from postgresql then "postgres" would be the\  ``provider.name()`` \returned.

\  **5.** \One way you'll access vector layer features is through the data provider's\  `select() <http://doc.qgis.org/head/classQgsVectorDataProvider.html#ed7343c5ccea4d4fe795159eb4268b96>`_ \function::

    >>> provider.select()

The\  ``select()`` \function reads the vector layer's attributes and geometry into memory so we can access them. If you take a look at the\  `select() API <http://doc.qgis.org/head/classQgsVectorDataProvider.html#ed7343c5ccea4d4fe795159eb4268b96>`_ \you'll notice that we can refine what we actually want to get back from the layer including only certain attributes.

When we run\  ``select()`` \without any arguments passed we are only getting the default options. "Default" options in this case means::

    - Attributes -- do not retrieve any attributes
    - Rectangle Filter -- do not use a spatial filter of a rectangle (think bounding box)
    - Geometry -- retrieve every feature geometry
    - Intersection Test -- do not run the accurate intersection test  

To summarize, when we ran\  ``select()`` \we retrieved all feature geometries but no attributes.

\  **6.** \Now let's get one feature id and geometry::

    >>> feat = QgsFeature()
    >>> # the above is an empty QgsFeature until we pass it to the provider
    >>> provider.nextFeature(feat)
    True
    >>> feat.id()
    0
    >>> feat.geometry()
    <qgis.core.QgsGeometry object at 0xca0fdec>
    >>> cLayer.setSelectedFeatures([0])

The above code retrieved the first feature from our data provider -- a feature with an featureID of 0.

We then used the\  `QgsFeature.geometry() <http://doc.qgis.org/head/classQgsFeature.html#b0a934a1b173ce5ad8d13363c20ef3c8>`_ to get it's geometry. 

Lastly, we used the current layer reference to actually select that feature in QGIS.

\  **7.** \Open the layer's attribute table and click on the 'zoom to selected features' icon on the bottom left.

.. image:: ../_static/zoom_to_selected_feature.png
    :scale: 100%
    :align: center

It seems the island of Aruba has a featureID of 0. 

.. image:: ../_static/get_geometry_select_aruba.png
    :scale: 43%
    :align: center

Method 2
**********

Although we didn't use it above, many times you'll use\  ``QgsVectorDataProvider`` \with a\  ``while`` \statement to loop through all layer features. In these cases your workflow is probably requiring you to use all features. However, there are many workflows where you already have a feature ID. In these cases, you'll want to retrieve a single feature's attributes and geometry using something similar to the\  ``select()`` \function. Here's how we do that.

The function\  `featureAtId() function <http://doc.qgis.org/head/classQgsVectorDataProvider.html#583a432e2e1046392abf79bf1e58f404>`_ \of the QgsVectorDataProvider class is just like the select statement with a few different arguments::

    ## Arguments
    - featureID -- the feature id you want to retrieve
    - feature -- the empty QgsFeature that you are passing into the function to initialize
    - fetchGeometry -- a boolean value that reflects whether we want the geom returned or not (defaults to True)
    - attributeList -- a list containing the indexes of the attribute fields to copy (defaults to an empty list -- no attributes)

\  **1.** \If we don't care about getting a feature's attributes, then we can ignore the last two attributes. Run this statement to get the Aruba feature again::

    >>> feat = QgsFeature()
    >>> provider.featureAtId(0, feat)
    True


Geometry Types
****************

\  **2.** \With any geometry reference we can do quality checks to make sure we want to use this geometry in further processing::

    >>> feat.geometry().asPolygon()
    [[(-69.8991,12.452), (-69.8957,12.423), (-69.9422,12.4385), (-70.0041,12.5005), (-70.0661,12.547), (-70.0509,12.5971), (-70.0351,12.6141), (-69.9731,12.5676), (-69.9118,12.4805), (-69.8991,12.452)]]
    >>> feat.geometry().length()
    0.53411147802819525
    >>> feat.geometry().area()
    0.012862549465307641
    >>> feat.geometry().isGeosValid()
    True
    >>> feat.geometry().isGeosEmpty()
    False
    >>> feat.geometry().isMultipart()
    False

This geometry is valid, not empty and looks to be a simple Polygon (as opposed to a MultiPolygon).

\  **3.** \To be sure that this geometry is of the 'type' we intend to use we can also use these methods to quality check::

    >>> feat.geometry().wkbType()
    3
    >>> QGis.WKBPolygon
    3
    
Note a couple things. Geometry types return an integer (essentially a lookup) that details what geometry they are. There are two ways to cross-reference this geometry type:

    \A. Above we use\  `QGis.WkbType() function <http://doc.qgis.org/head/classQGis.html#8da456870e1caec209d8ba7502cceff7>`_ \to compare well-known binary types.

    \B. Or we can use\  `QGis.type() function <http://doc.qgis.org/head/classQGis.html#09947eb19394302eeeed44d3e81dd74b>`_ \to compare to some basic typing::

        >>> feat.geometry().type()
        2
        >>> QGis.Polygon
        2

\  **4.** \Now let's do a very simple spatial operation like a buffer:: 

    >>> buff_geom = feat.geometry().buffer(12, 2)
    >>> buff_geom.asPolygon()
    [[(-78.2223,4.28234), (-81.4729,8.82057), (-81.5448,16.0456), (-81.5295,16.0957), (-78.8639,20.7414), (-78.8482,20.7585), (-71.1219,24.5648), (-62.8358,22.2146), (-62.7738,22.1681), (-60.16,19.4743), (-60.0987,19.3872), (-58.9469,17.356), (-58.9342,17.3275), (-57.9838,13.875), (-57.9804,13.8461), (-59.6758,6.13379), (-65.7966,1.14483), (-73.6923,1.03945), (-73.7388,1.05495), (-77.0515,3.10271), (-77.2035,2.90002), (-77.2655,2.94651), (-77.6363,3.46418), (-78.4274,3.95324), (-78.4894,4.01522), (-78.2223,4.28234)]]
    >>> buff_geom.area()
    430.95305806853509

We buffered our polygon by 12 degrees. We can see this created more vetices in the polygon list. Printing out the geometry also verifies that we expanded this polygon. Just to be sure::

    >>> buff_geom.area() > feat.geometry().area()
    True

\  **5.** \Let's test the Aruba geometry against an intersecting QgsPoint geometry as a last example::

    >>> # does the Aruba geometry intersect with Seattle (-122.361,47.642) -- I hope not!
    >>> feat.geometry().intersects(QgsGeometry.fromPoint(QgsPoint(-122.361,47.642)))
    False
    >>> # does the Aruba geometry intersect with a point inside of itself -- the real test
    >>> feat.geometry().intersects(QgsGeometry.fromPoint(QgsPoint(-69.953,12.512)))
    True

------------------------------------------------------

Accessing Data Attributes
-----------------------------

Here we will be covering data attribute retrieval for vector and raster layers. The following excercises will help us answer the questions:

    \1) What's the name of the selected feature?

    \2) What values does this raster cell have?

    \3) How many features meet this filtering requirement?
 
Vector
**********

Using our\  ``50m_admin_0_countries.shp`` \layer:

\  **1.** \Get the data provider for this shapefile::

    >>> provider = aLayer.dataProvider()
    >>> aLayer = qgis.utils.iface.activeLayer()
    >>> provider = aLayer.dataProvider()
    >>> aLayer.name()
    PyQt4.QtCore.QString(u'50m_admin_0_countries')
    >>> provider.name()
    PyQt4.QtCore.QString(u'ogr')

\  **2.** \Let's get a Python dictionary of the fields::

    >>> columns = provider.fields()
    >>> type(columns)
    <type 'dict'>

\  **3.** \Remember that a Python dictionary data structure has a unique set of keys that point to corresponding values. The\  ``provider.fields()`` \function returns us the 0-based positional index of column objects from left-to-right. That means the left-most column (or field) starts at 0. Each integer index points to a\  `QgsField object <http://doc.qgis.org/head/classQgsField.html>`_ \for reference::

    >>> columns[0]
    <qgis.core.QgsField object at 0xd8df66c>

The above isn't very useful output yet. To get useful column output we need to access the attributes and functions of the QgsField object itself (we'll do that in 2 steps).

\  **4.** \Remember that\  **ALL** \the dictionary keys or values call be returned in a list through these functions::

    >>> columns.keys()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    >>>
    >>> columns.values()
    [<qgis.core.QgsField object at 0xd8df66c>, <qgis.core.QgsField object at 0xd8df6ac>, <qgis.core.QgsField object at 0xd8df62c>, <qgis.core.QgsField object at 0xd8df5ec>, <qgis.core.QgsField object at 0xd8df5ac>, <qgis.core.QgsField object at 0xd8df56c>, <qgis.core.QgsField object at 0xd8df52c>, <qgis.core.QgsField object at 0xd8df4ec>, <qgis.core.QgsField object at 0xd8df4ac>, <qgis.core.QgsField object at 0xd8df46c>, <qgis.core.QgsField object at 0xd8df42c>, <qgis.core.QgsField object at 0xd8df3ec>, <qgis.core.QgsField object at 0xd8df3ac>, <qgis.core.QgsField object at 0xd8df36c>, <qgis.core.QgsField object at 0xd8df32c>, # TRUNCATED OUTPUT ON PURPOSE ]


\  **5.** \To loop through the keys and values at once we can do this::

    >>> for key,value in columns.items(): print str(key) + " = " + str(value)
    ... 
    0 = <qgis.core.QgsField object at 0xd8df66c>
    1 = <qgis.core.QgsField object at 0xd8df6ac>
    2 = <qgis.core.QgsField object at 0xd8df62c>
    3 = <qgis.core.QgsField object at 0xd8df5ec>
    4 = <qgis.core.QgsField object at 0xd8df5ac>
    5 = <qgis.core.QgsField object at 0xd8df56c>
    6 = <qgis.core.QgsField object at 0xd8df52c>
    7 = <qgis.core.QgsField object at 0xd8df4ec>
    8 = <qgis.core.QgsField object at 0xd8df4ac>
    
    # TRUNCATED OUTPUT ON PURPOSE

\  **6.** \Now let's get some meaningful output from the QgsField object::
 
    >>> for key,value in columns.items(): print str(key) + " = " + str(value.name()) 
    ... 
    0 = ScaleRank
    1 = FeatureCla
    2 = SOVEREIGNT
    3 = SOVISO
    4 = SOV_A3
    5 = LEVEL
    6 = TYPE
    7 = NAME
    8 = SORTNAME
    9 = ADM0_A3
    10 = NAME_SM
    11 = NAME_LNG
    12 = TERR_
    13 = PARENTHETI
    14 = NAME_ALT
    15 = LOCAL_LNG

    # TRUNCATED OUTPUT ON PURPOSE

\  **7.** \We can add other QgsField attributes to the iteration above::

    >>> for key,value in columns.items(): print str(key) + " = " + str(value.name()) + " | " + str(value.typeName()) + " | " + str(value.length())
    ... 
    0 = ScaleRank | Integer | 4
    1 = FeatureCla | String | 30
    2 = SOVEREIGNT | String | 32
    3 = SOVISO | String | 3
    4 = SOV_A3 | String | 3
    5 = LEVEL | Real | 4
    6 = TYPE | String | 13
    7 = NAME | String | 36
    8 = SORTNAME | String | 36

The take home point is that the QgsField object gives us the names and data types of the attribute columns but\  **NOT** \the individual feature attribute values. These have to be accessed through the features themselves.

\  **8.** \We've already seen how to retrieve vector features using two functions:

    \1) The QgsVectorDataProvider's\  ``select()`` \function
    \2) The QgsVectorDataProvider's\  ``featureAtId()`` \function

The example below reviews how to retrieve features and also adds the necessary steps to select only certain attributes using the\  ``dataProvider.select() function`` \. This time however we will be passing in\  **ALL** \the\  ``select()`` \function arguments. Notes on each step are included with the code below::

    >>> # Create an empty list that will hold the column indexes for the columns we are interested in 
    >>> selectList = []
    >>> # For each column name we are interested in retreiving get its index and add it to the above selectList
    >>> for column in ['LEVEL', 'TYPE', 'NAME', 'SORTNAME']:
    ...     selectList.append(provider.fieldNameIndex(column))
    ... 
    >>> # Our column index output 
    >>> selectList
    [5, 6, 7, 8]
    >>> # Create a bounding box rectangle that we will use as a filter to only get features that intersect with it
    >>> rect = QgsRectangle(QgsPoint(0,0),QgsPoint(20, 34))
    >>> # The infamous select statement that queries our vector layer for all geometry, attributes indexes we passed and only the features that intersect our QgsRectangle
    >>> provider.select(selectList, rect, True, False)
    >>> feat = QgsFeature()
    >>> # walk through each feature of our select statement and get the attributes
    >>> while provider.nextFeature(feat):
    ...     # we get our dictionary of attribute index keys pointing to field values for this feature
    ...     map = feat.attributeMap()
    ...     # for each feature's attributes print out the value
    ...     for key, value in map.items(): print value.toString()
    ...
    # OUTPUT TRUNCATED FOR DEMONSTRATION

\  **9.** \This next example is a little harder to understand. The point is to show you how to create dictionaries. We're going to create a table data structure -- a Python dictionary that represents a table in a database. The table is a dictionary where the keys are the featureIDs for each feature and the values will be nested dictionaries that have keys with column names and values with the column value. Reworking the above example gives us::

    >>> provider.select(selectList, rect, True, False)
    >>> table = {}
    >>> 
    >>> while provider.nextFeature(feat):
    ...     attributeMap = feat.attributeMap()
    ...     table[feat.id()] = { 'LEVEL' : attributeMap[provider.fieldNameIndex('LEVEL')].toString() \
    ...                           , 'NAME' : attributeMap[provider.fieldNameIndex('NAME')].toString() \
    ...                           , 'SORTNAME' : attributeMap[provider.fieldNameIndex('SORTNAME')].toString() \
    ...                           , 'TYPE' : attributeMap[provider.fieldNameIndex('TYPE')].toString() \ 
    ...                         }
    >>>
    >>> for id, record in table.items(): print str(id) + " --> " + str(record)
    ...
    158 --> {'SORTNAME': PyQt4.QtCore.QString(u'Nigeria'), 'TYPE': PyQt4.QtCore.QString(u'Sovereign'), 'NAME': PyQt4.QtCore.QString(u'Nigeria'), 'LEVEL': PyQt4.QtCore.QString(u'2')}
    38 --> {'SORTNAME': PyQt4.QtCore.QString(u'Central African Republic'), 'TYPE': PyQt4.QtCore.QString(u'Sovereign'), 'NAME': PyQt4.QtCore.QString(u'Central African Republic'), 'LEVEL': PyQt4.QtCore.QString(u'2')}
    142 --> {'SORTNAME': PyQt4.QtCore.QString(u'Mali'), 'TYPE': PyQt4.QtCore.QString(u'Sovereign'), 'NAME': PyQt4.QtCore.QString(u'Mali'), 'LEVEL': PyQt4.QtCore.QString(u'2')}
    156 --> {'SORTNAME': PyQt4.QtCore.QString(u'Niger'), 'TYPE': PyQt4.QtCore.QString(u'Sovereign'), 'NAME': PyQt4.QtCore.QString(u'Niger'), 'LEVEL': PyQt4.QtCore.QString(u'2')}
    75 --> {'SORTNAME': PyQt4.QtCore.QString(u'Gabon'), 'TYPE': PyQt4.QtCore.QString(u'Sovereign'), 'NAME': PyQt4.QtCore.QString(u'Gabon'), 'LEVEL': PyQt4.QtCore.QString(u'2')}
    44 --> {'SORTNAME': PyQt4.QtCore.QString(u'Cameroon'), 'TYPE': PyQt4.QtCore.QString(u'Sovereign'), 'NAME': PyQt4.QtCore.QString(u'Cameroon'), 'LEVEL': PyQt4.QtCore.QString(u'2')}
    45 --> {'SORTNAME': PyQt4.QtCore.QString(u'Congo (Kinshasa)'), 'TYPE': PyQt4.QtCore.QString(u'Sovereign'), 'NAME': PyQt4.QtCore.QString(u'Democratic Republic of the Congo'), 'LEVEL': PyQt4.QtCore.QString(u'2')}
    # TRUNCATED FOR DEMO 


Raster
*********

In this next example we'll be querying raster cell values with QgsPoints using the\  `QgsRasterLayer.identify() function <http://doc.qgis.org/head/classQgsRasterLayer.html#4bcb29bba8fc0fca1e0bed41b6a0ee9b>`_ \. Although the C++ API shows the identify() function taking two arguments the Python bindings really only need a QgsPoint() to be passed as an argument.


\  **1.** \Load the following shaded relief into QGIS::

    /home/qgis/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif

\  **2.** \The first thing we need to do is create a couple points in WGS84 (EPSG:4326) that we can used to query this raster layer. I've chosen Dar-Es-Salaam, Tanzania and Assam, India as a couple locations::

    >>> DarEsSalaam = QgsPoint(39.268, -6.80)
    >>> DarEsSalaam
    (39.268,-6.8)
    >>> Assam = QgsPoint(91.76,26.144)
    >>> Assam
    (91.76,26.144)

\  **3.** \Make sure you have a reference to the\  ``SR_50M.tif`` \raster layer::

    >>> rLayer = qgis.utils.iface.mapCanvas().layer(1)
    >>> rLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

\  **4.** \The\  `QgsRasterLayer.identify() function <http://doc.qgis.org/head/classQgsRasterLayer.html#4bcb29bba8fc0fca1e0bed41b6a0ee9b>`_ \returns a boolean True or False to indicate whether or not the identify worked. The data is returned in a dictionary with the band number as a key and the value for that band number as a value::

    >>> rLayer.identify(Assam)
    (True, {PyQt4.QtCore.QString(u'Band 1'): PyQt4.QtCore.QString(u'218')})
    >>> rLayer.identify(DarEsSalaam)
    (True, {PyQt4.QtCore.QString(u'Band 1'): PyQt4.QtCore.QString(u'202')})

\  **5.** \To extract the data returned from identify and make it a little more presentable we can do the following::

    >>> success, data = rLayer.identify(DarEsSalaam)
    >>> for band, value in data.items(): print str(band) + " = " + str(value)
    ... 
    Band 1 = 202
    >>> 

------------------------------------------------------

Symbology
--------------

Let's go through some quick symbology moves using raster and vector data types.

Raster
********

Remember that the class\  `QGis <http://doc.qgis.org/head/classQGis.html>`_ \references some global constants that represent basic vector data types. These data types can be used for comaprison like this::

    >>> myPoint = QgsGeometry.fromPoint(QgsPoint(-122,47))
    >>> myPoint
    <qgis.core.QgsGeometry object at 0xcb6822c>
    >>> myPoint.asPoint()
    (-122,47)
    >>> myPoint.type()
    0
    >>> QGis.Point
    0
    >>> myPoint.wkbType()
    1
    >>> QGis.WKBPoint
    1
    >>> myPoint.type() == QGis.Point
    True
    >>> myPoint.wkbType() == QGis.WKBPoint
    True


Raster data also has it's own global constants that represent raster data types (Color, Paletted, GrayOrUndefined, Multiband) as well as the differnt types of shading and drawing that can happen. These are defined in the\  `QgsRasterLayer class <http://doc.qgis.org/head/classQgsRasterLayer.html#37e287fd16e799bddcf0e5533de07c13>`_ \. To get an idea about what integer lookup each one represents we can do exactly what we did above::

    >>> # Here a couple raster types
    >>> QgsRasterLayer.Palette
    1
    >>> QgsRasterLayer.Multiband
    2
    >>> # Here are a couple raster drawing styles
    >>> QgsRasterLayer.SingleBandGray
    1
    >>> QgsRasterLayer.SingleBandPseudoColor
    2
    >>> # Here a couple raster shaded styles
    >>> QgsRasterLayer.UndefinedShader
    0
    >>> QgsRasterLayer.PseudoColorShader
    1

When a raster layer is loaded into QGIS it gets a default\  `DrawingStyle <http://doc.qgis.org/head/classQgsRasterLayer.html#36796f1a303dac9848ba3dce3e5527dc>`_ \based on it's\  `LayerType <http://doc.qgis.org/head/classQgsRasterLayer.html#37e287fd16e799bddcf0e5533de07c13>`_ \.

\  **1.** \Let's see what kind of raster type and drawing style our raster layer has. Make sure you have reference to the raster layer first::

    >>> rLayer = qgis.utils.iface.mapCanvas().layers()[1]
    >>> rLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')
    >>> rLayer.rasterType()
    0
    >>> rLayer.rasterType() == QgsRasterLayer.GrayOrUndefined
    True
    >>> rLayer.colorShadingAlgorithm()
    2
    >>> rLayer.colorShadingAlgorithm() == QgsRasterLayer.FreakOutShader
    True
    >>> rLayer.drawingStyle()
    1
    >>> rLayer.drawingStyle() == QgsRasterLayer.SingleBandGray
    True


\  **2.** \Changing between these global shading or drawing styles is arbitrary. When you are done, refresh the map::

    >>> rLayer.setColorShadingAlgorithm(QgsRasterLayer.PseudoColorShader)
    >>> rLayer.setDrawingStyle(QgsRasterLayer.SingleBandPseudoColor)
    >>> # Now setup the refresh to see the change
    >>> rLayer.setCacheImage(None)
    >>> rLayer.triggerRepaint()
    >>> qgis.utils.iface.legendInterface().refreshLayerSymbology(rLayer)


