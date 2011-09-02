=============================
Exercises
=============================

Create On-the-Fly Raster Value Emitter
--------------------------------------------------------

In this final exercise you will use all that you have learned up to this point to create a simple (maybe even crude) raster value display tool. The purpose is for you to figure out the programmatic steps based on a few clues.

The Tool Requirements
*************************

* Display the value of every band for any raster on map canvas mouse hover. That sounds confusing, but the idea is that your tool should work with a single grayscale raster or an RGBA raster without blowing up. There will be no mouse clicks, we'll just be responding to the normal mouse cursor movement over the map canvas

* Feedback of raster values will be output to a GUI (your choice on how to implement this on the GUI)

Hints
***************

* You will want to connect a custom function to the map canvas signal\  `xyCoordinates <http://doc.qgis.org/head/classQgsMapCanvas.html#bf90fbd211ea419ded7c934fd289f0ab>`_ \

* You can get raster values for each band like this::

    rLayer = self.iface.mapCanvas().currentLayer()
    success, data = rLayer.identify(QgsPoint(-122, 47))
    for band, value in data.items():
        print str(band) + " = " + str(value)

Solution
************

If you want to peek at one possible solution (thought a very ugly one) then check out these modules:

    * The main Python module\  `here <../_static/rastervaluedisplay.py>`_

    * The dialog module\  `there <../_static/rastervaluedisplaydialog.py>`_

    * The compiled ui module\  `over here <../_static/ui_rastervaluedisplay.py>`_

To get a visual idea about how simple my tool was, here's a picture:

.. image:: ../_static/raster_value_final.png
    :scale: 100%
    :align: center

