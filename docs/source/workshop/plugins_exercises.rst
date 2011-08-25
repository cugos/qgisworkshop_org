=============================
Exercises
=============================

Expanding the Tutorial Plugin
--------------------------------

There's a couple of ridiculous things happening in the tutorial example that I would like to change and talk about. 

    1. Everytime we click the map canvas a signal is sent out, and our slot (or handler)\  ``selectFeature()`` \runs and does a number of things before selecting a feature:
        * gets the current layer
        * gets the current layer's data provider

Let's make this simplier by thinking about things a event driven. When are layer is first selected in the TOC it will fire a signal. This then seems like a good place to put anything intialization code for the current layer or data provider since we'll be handling things one-at-a-time. 

Let's expand on the last tutorial and add one more feature. We want to output a 'NAME' attribute to the TextBrowser if it exists. Most of what we have to do to implement this is code reorganization. 

First, let's ensure that everytime a selection is made that we have a class variable that holds that information for all class functions to use. In fact, we need to move many variables to the class level that appear in\  ``selectFeature()`` \function. That means we'll have to move the\  ``selectList`` \variable out from the\  ``selectFeature()`` \function and put it under\  ``__init__()`` \.



---------------------------


Using File Dialogs / Event-Driven Design
-------------------------------------------

# stub


-------------------------------------


Creating a Raster Value Analyzer with on the fly
----------------------------------------------------

# stub
