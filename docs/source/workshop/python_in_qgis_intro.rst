
=====================================
Python in QGIS -- PyQGIS
=====================================

When we use the term\  **PyQGIS** \we are refering to the QGIS Python bindings. Specifically, we are referring to a Python application programming interface (API) that wraps the QGIS C++ library. Here is the\   `C++ QGIS API documentation <http://doc.qgis.org>`_ \.

We'll be using the C++ QGIS API documentation as a roadmap to understanding PyQGIS because the PyQGIS API documentation is nonexistent. This can be a little confusing at times. But for the most part the Python bindings are a mirror of the C++ library.

We will become very familiar with parts of the above documentation as we build plugins. For now it's good to note that there's a number of ways to interact with QGIS using Python. Here are the most common ways:

    1. \  **Python Console** \: a command-line terminal inside QGIS to test ideas and do one-off quick jobs

    2. \  **Plugins** \: enhancing/creating editing tools that interact with data inside the QGIS environment 

    3. \  **Python Scripts/Applications** \: scripts that process spatial data outside the QGIS application. Or a user could create their own stripped-down data viewer and analysis tools using QGIS libraries

We will be focusing on using the Python console during this next hour. Everything we're learning will be directly applicable to our plugin development the following two hours.

------------------------------------------------------

Python Console
------------------

This is perhaps the easiest way to start testing out your plugin ideas.

From the Python Console we can access vector and raster layers that are already loaded into QGIS. Once accessed, we can start interacting with their attributes and geometry. Since a lot of plugin work is dealing with layer attributes and geometry then let's begin here.

We'll walk through the following building-block examples.

