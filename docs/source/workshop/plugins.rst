=======
Plugins
=======

Plugin Architecture
---------------------

QGIS Python plugins are set of Python modules that describe everthing from our plugin resources to the code that runs the plugin logic. We'll save the details for the\  **Examples** \section below, but here's a high-level overview.

To create QGIS Python plugins you'll need at least 4 types of files (though most plugins often contain more):
    - a file with a\  ``.ui`` \extension that describes your graphical user interface (GUI). This has to be compiled into a python modules using the command-line tool\  ``pyuic4`` \.
    - a file that gives high-level configuration information about your plugin such as the name\  ``__init__.py`` \.
    - a file with a\  ``.qrc`` \extension describing the resources your plugin might use such as images. This has to be compiled into a python module using the command-line tool\  ``pyrcc4`` \.
    - and finally, the meat-and-potatoes of the plugin is the file that does the actual work and most of the time handles communication between your resources and GUI. This file is just a normal python module with some specific import statements and method names. It can be named anything, though that name is usually associated to the name of your plugin.

-----------------------------

To get a better idea about how these types of files fit into a plugin project let's look at a Python plugin that is already installed on your system. Then we can look for the file patterns described above.

\  **1.** \Open a new bash shell. The bash shell can be started by holding down\  ``<Cntl>-<ALT>`` \keys and then pressing\  ``t`` \at the same time. You should see a purple window pop open with a blinking cursor.

.. image:: ../_static/terminal_window_open.png
    :scale: 70%
    :align: center

\  **2.** \Now change directories into the hidden\  ``.qgis`` \folder in your home folder. Nested inside this folder is where Python plugins are stored. List all the folders in plugins::

    $cd .qgis/python/plugins/
    $ ls -lah
    total 17K
    drwxr-xr-x 10 qgis qgis 4.0K 2011-07-17 20:40 .
    drwxr-xr-x  4 qgis qgis 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x  3 qgis qgis 4.0K 2011-07-07 13:41 pluginbuilder
    

The\  **pluginbuilder** \plugin project located in\  ``/home/qgis/.qgis/python/plugins`` \is a plugin we'll get familiar with in a second. It eases the pain of creating plugins by automajically creating plugin template files (the ones we talked briefly about above) and piping in a lot of the code we'll use. 


\  **3.** \Now change directories into the\  ``pluginbuilder`` \directory and list those contents::

    $ cd pluginbuilder
    $ ls -lah
    total 164K
    drwxr-xr-x  3 qgis qgis 4.0K 2011-07-07 13:41 .
    drwxr-xr-x 10 qgis qgis 4.0K 2011-07-17 20:40 ..
    -rw-r--r--  1 qgis qgis   31 2011-07-07 13:41 .gitignore
    -rw-r--r--  1 qgis qgis 1.1K 2011-07-07 13:41 help.html
    -rw-r--r--  1 qgis qgis 1.1K 2011-07-07 13:41 icon.png
    -rw-r--r--  1 qgis qgis 1.6K 2011-07-07 13:41 __init__.py
    -rw-r--r--  1 qgis qgis 2.5K 2011-07-07 13:41 __init__.pyc
    -rw-r--r--  1 qgis qgis 2.1K 2011-07-07 13:41 Makefile
    -rw-r--r--  1 qgis qgis 1.4K 2011-07-07 13:41 pluginbuilder_dialog.py
    -rw-r--r--  1 qgis qgis 1.9K 2011-07-07 13:41 pluginbuilder_dialog.pyc
    -rw-r--r--  1 qgis qgis 4.1K 2011-07-07 13:41 plugin_builder.png
    -rw-r--r--  1 qgis qgis 7.0K 2011-07-07 13:41 pluginbuilder.py
    -rw-r--r--  1 qgis qgis 6.4K 2011-07-07 13:41 pluginbuilder.pyc
    -rw-r--r--  1 qgis qgis 2.2K 2011-07-07 13:41 pluginspec.py
    -rw-r--r--  1 qgis qgis 2.5K 2011-07-07 13:41 pluginspec.pyc
    -rw-r--r--  1 qgis qgis  137 2011-07-07 13:41 README.rst
    -rw-r--r--  1 qgis qgis  23K 2011-07-07 13:41 resources.py
    -rw-r--r--  1 qgis qgis 6.1K 2011-07-07 13:41 resources.pyc
    -rw-r--r--  1 qgis qgis  143 2011-07-07 13:41 resources.qrc
    -rw-r--r--  1 qgis qgis 1.4K 2011-07-07 13:41 result_dialog.py
    -rw-r--r--  1 qgis qgis 1.8K 2011-07-07 13:41 result_dialog.pyc
    drwxr-xr-x  2 qgis qgis 4.0K 2011-07-07 13:41 templateclass
    -rw-r--r--  1 qgis qgis 8.6K 2011-07-07 13:41 ui_pluginbuilder.py
    -rw-r--r--  1 qgis qgis 5.9K 2011-07-07 13:41 ui_pluginbuilder.pyc
    -rw-r--r--  1 qgis qgis 6.9K 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r--  1 qgis qgis 1.7K 2011-07-07 13:41 ui_results.py
    -rw-r--r--  1 qgis qgis 2.2K 2011-07-07 13:41 ui_results.pyc
    -rw-r--r--  1 qgis qgis 1.9K 2011-07-07 13:41 ui_results.ui

I know this is a lot of files but we are only interested in looking for patterns here. 

As you can see there seems to be two GUI(s) associated with this plugin. We got this number by counting the number of files with a\  ``.ui`` \extension::

    -rw-r--r--  1 qgis qgis 6.9K 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r--  1 qgis qgis 1.9K 2011-07-07 13:41 ui_results.ui

We can also see that each of the\  ``.ui`` \files has been compiled into python modules with the same basename. So all of these files seem to be related to the GUI::

    -rw-r--r--  1 qgis qgis 8.6K 2011-07-07 13:41 ui_pluginbuilder.py
    -rw-r--r--  1 qgis qgis 5.9K 2011-07-07 13:41 ui_pluginbuilder.pyc
    -rw-r--r--  1 qgis qgis 6.9K 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r--  1 qgis qgis 1.7K 2011-07-07 13:41 ui_results.py
    -rw-r--r--  1 qgis qgis 2.2K 2011-07-07 13:41 ui_results.pyc
    -rw-r--r--  1 qgis qgis 1.9K 2011-07-07 13:41 ui_results.ui

Notice the\ ``__init__.py`` \file. If you opened this file, then you'd see its guts, which describe some high-level plugin information::

    def name():
        return "Plugin Builder"
    def description():
        return "Creates a QGIS plugin template for use as a starting point in plugin development"
    def version():
        return "Version 0.3.2"
    def icon():
        return 'plugin_builder.png'
    def qgisMinimumVersion():
        return "1.0"
    def classFactory(iface):
        # load PluginBuilder class from file PluginBuilder
        from pluginbuilder import PluginBuilder
        return PluginBuilder(iface)

We can also see that these files are associated to the resources::

    -rw-r--r--  1 qgis qgis  23K 2011-07-07 13:41 resources.py
    -rw-r--r--  1 qgis qgis 6.1K 2011-07-07 13:41 resources.pyc
    -rw-r--r--  1 qgis qgis  143 2011-07-07 13:41 resources.qrc

The\  ``resources.py`` \and\  ``resources.pyc`` \are the compiled version of\  ``resources.qrc`` \.

With that said, it's probably a good guess that anything else with a\ ``.py`` \extension in this directory that we didn't talk about is related to the main plugin logic. There also seems to be some documents and images that we don't need to be concerted about at this point.

----------------------------

Installing QGIS Plugins
------------------------------

So how did the\  ``pluginbuilder`` \plugin get in this directory? 

Let's review how we install pluings briefly.


----------------------------

Building Our First Pluing with PluginBuilder
------------------------------------------------

Now it's time to get our feet really wet


Examples
--------

