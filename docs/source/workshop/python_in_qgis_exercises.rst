===========================
Exercise
===========================

Output Vector Layer attributes to the TextBrowser
--------------------------------------------------------

You will edit one function from the existing\  ``foss4g2011_example1`` \plugin. In that function you will write the logic that reads a vector data layer's attributes and displays them to the TextBrowser output.

Goal
*************************

\  **1.** \Open the\  ``foss4g2011_example1`` \plugin with some a vector layer loaded into Qgis

.. image:: ../_static/ex1_openplugin.png
    :scale: 100%
    :align: center

\  **2.** \Click somewhere on the map and you will see generic output to the TextBrowser

.. image:: ../_static/ex1_exoutput.png
    :scale: 100%
    :align: center

\  **3.** \Using gedit, navigate to\  ``/home/qgis/.qgis/python/plugins/foss4g2011_example1/`` \and open the\  ``foss4g2011_example1.py`` module. Find the function\  ``updateTextBrowser(0`` \. This is the code you will be changing around::

    def updateTextBrowser(self):
        # check to make sure we have a feature selected in our selectList -- note that there might be more than one feature
        if self.selectList:

            # ***************EXAMPLE 1 EDITS GO HERE********************
            ''' write code that will output ALL attributes for a single selected feature into the Text Browser. 
                instead of using the dataProvider.select() function get the actual QgsFeature using dataProvider.featureAtId() '''
     
            self.dlg.setTextBrowser("example text output\n to TextBrowser")


Hints
***************

In the last hour we went through an example using\  ``dataProvider.featureAtId()`` \. Use this code as a guide for how to create your function::



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

