
=====================================
Python in QGIS -- PyQGIS
=====================================

When we use the term\  **PyQGIS** \we are refering to the QGIS Python bindings.

Specifically, we are referring an application programming interface (API) that accesses QGIS's C/C++ library layout. Here is the QGIS library documentation: 

    http://doc.qgis.org

We will become very familiar with parts of the above documentation as we build plugins.

For now it's good to note that there's a number of ways to interact with QGIS using Python.

Here are the most common ways:

    1. \  **Python Console** \: a command-line terminal inside QGIS to test ideas and do one-off quick jobs

    2. \  **Plugins** \: enhancing/creating editing tools that interact with data inside the QGIS environment 

    3. \  **Python Scripts/Applications** \: scripts that process spatial data outside the QGIS application. Or a user could create their own stripped-down data viewer and explorer using QGIS libraries


Python Console
------------------

This is perhaps the easiest way to start testing out your ideas for plugins.

From the Python Console we can access vector and raster layers that are already loaded into QGIS. Once accessed, we can start interacting with their attributes and geometry. Since a lot of plugin work is dealing with layer attributes and geometry then let's begin.

We'll walk through the following building-block examples.

Setup
-------------

To begin open up a new QGIS session by clicking the QGIS icon on the top menu bar:

<pic>

All the data we will be using is located in the\  ``natural_earth_50m`` \directory of your qgis user home path::

    /home/qgis/natural_earth_50m

Add the following vector and raster files to QGIS::

    /home/qgis/natural_earth_50m/raster/shaded_relief/SR_50M/SR_50M.tif
    
    # turn off the tif layer so it doesn't slow things down

    /home/qgis/natural_earth_50m/cultural/50m_cultural/50m_populated_places_simple.shp

Now open the Python Console by selecting::

    Plugins > Pythong Console

<pic> 

Accessing Layers
--------------------------

.. note:: The hyperlinks that follow all reference the QGIS API Documentation. Click on them to view the classes and methods we are referencing below

There's a number of ways to access the layers in QGIS. 

All the ways start by first referencing the\  `QgsInterface object <http://doc.qgis.org/head/classQgisInterface.html>`_ \which is called\  **iface** \in the Python bindings.

From the Python Console we access\  **iface** \by calling the following command::
    
    >>> qgis.utils.iface

Type the above command in the Python Console::

    >>> qgis.utils.iface
    <qgis.gui.QgisInterface object at 0x925266c>

Running the above command prints out the actual name of the QGIS class we are dealing with -- indeed iface is the QgsInterface object 

Method 1
*********

On the iface object is a useful function called\  `activeLayer() <http://doc.qgis.org/head/classQgisInterface.html#231f32fbf95004aebb067cb98f3a391c>`_ \that returns us a reference to the selected layer in the layer legend.

Run the following command::

    >>> aLayer = qgis.utils.iface.activeLayer()
    >>> aLayer
    <qgis.core.QgsRasterLayer object at 0x99ea6ec>

Depending on which layer is selected in the table of contents you will see either a raster or vector layer output. I had the raster layer selected it seems.

What is the name of the active layer?::

    >>> aLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

Method 2
**********

Another common way of accessing the selected layer in the table of contents is to get at it using the\  `QgsMapCanvas <http://doc.qgis.org/head/classQgsMapCanvas.html>`_ \. The mapCanvas object has tons of useful functions::

    >>> canvas = qgis.utils.iface.mapCanvas()
    >>> cLayer = canvas.currentLayer()
    >>> cLayer.name()
    PyQt4.QtCore.QString(u'SR_50M')

Method 3
**********

With the map canvas object we can get more than just the active layer -- we can get everthing::

    >>> allLayers = canvas.layers()
    >>> for i in allLayers: print i.name()
    ... 
    50m_populated_places_simple

Wait a minute! We have two layers in the table of contents. Why did we only get one single name back? (this is assuming that you followed directions and kept the raster layer turned off)

It turns out that using\  ``QgsMapCanvas.layers()`` \will only return us\  **visible** \layers (those that are checked visible).

Turn on the raster layer in the table of contents. Rerun the exact same two lines of code above::

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

We access layers using the\  `QgsMapCanvas.layer() function <http://doc.qgis.org/head/classQgsMapCanvas.html#de2251f2227bc0f0efefd09810a193cd>`_ \and pass in a integer designating the index we want::

    >>> canvas.layer(0)
    <qgis.core.QgsVectorLayer object at 0x99eaeec>
    >>> canvas.layer(0).name()
    PyQt4.QtCore.QString(u'50m_populated_places_simple')    


Other Excercises
********************

- set the active layer using qgis.utils.iface.setActiveLayer()

- set the current layer using qgis.utils.iface.setCurrentLayer()

- can you find the QgsMapLayer class in the documentation and find out how to get a layer's extent?

.. note:: There's probably many more ways to access the layers in the QGIS table of contents...so keep your eyes open for other methods

Loading Layers into QGIS
-----------------------------

Maybe when you were purusing the QgsInterface object you noticed a couple addLayer methods? Let's use these to load layers into QGIS. 

Start by removing all layers from QGIS.

Then with a fresh map, re-add the SR_50M and populated places data:


Writing Layers to File
---------------------------------

Let's make a function that takes a layer as an argument and copies it to somewhere else on disk.

copy of the raster in vector layer in our map:



Applying filters to our Shapefile Imports
---------------------------------------------

Accessing Geometry and Basic Spatial Analysis
-----------------------------------------------

Constructing Geometry
************************

Casting Between Geometry Types
********************************

Spatial Predicates
****************************

Basic Spatial Operations
***************************

Accessing and Editing Attributes
-----------------------------------

SRS Transformation
-----------------------


