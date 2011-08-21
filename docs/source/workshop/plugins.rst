=======
Plugins
=======

Plugin Architecture
---------------------

QGIS Python plugins are just a set of Python modules that describe everything from our plugin resources to the code that runs the plugin logic. We'll save the details for the\  **Examples** \section below, but here's a high-level overview.

To create QGIS Python plugins you'll need at least 4 types of files in your project (though most plugins often contain more):
    - a file with a\  ``.ui`` \extension that describes your graphical user interface (GUI). This has to be compiled into a python module using the command-line tool\  ``pyuic4`` \.
    - a file that gives high-level configuration information about your plugin such as the name and author\  ``__init__.py`` \.
    - a file with a\  ``.qrc`` \extension describing the resources your plugin will use such as images. This has to be compiled into a python module using the command-line tool\  ``pyrcc4`` \.
    - and finally, the meat-and-potatoes of the plugin is the file that does the actual work. This module handles communication between your resources and GUI. This file is just a normal Python module with some specific import statements and method names. It can be named anything, though that name is usually associated with the name of your plugin.

-----------------------------

To get a better idea about how these different file types fit comprise a plugin project let's look at a Python plugin that is already installed on your system. Then we can look for the file patterns described above.

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
    

The\  **pluginbuilder** \project located in\  ``/home/qgis/.qgis/python/plugins`` \is a plugin we'll become familiar with soon. It makes creating plugins easier by automajically creating plugin template files (the file types we talked about above). The\  **pluginbuilder** \also pipes template code into the template files for us to modify.


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

Remember, we are only interested in looking for file patterns here. As you can see there seems to be two GUI(s) associated with this plugin. We got this number by counting the number of files with a\  ``.ui`` \extension::

    -rw-r--r--  1 qgis qgis 6.9K 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r--  1 qgis qgis 1.9K 2011-07-07 13:41 ui_results.ui

We can also see that each of the\  ``.ui`` \files has been compiled into python modules with the same basename. So all of the following files seem to be related to the GUI::

    -rw-r--r--  1 qgis qgis 8.6K 2011-07-07 13:41 ui_pluginbuilder.py
    -rw-r--r--  1 qgis qgis 5.9K 2011-07-07 13:41 ui_pluginbuilder.pyc
    -rw-r--r--  1 qgis qgis 6.9K 2011-07-07 13:41 ui_pluginbuilder.ui
    -rw-r--r--  1 qgis qgis 1.7K 2011-07-07 13:41 ui_results.py
    -rw-r--r--  1 qgis qgis 2.2K 2011-07-07 13:41 ui_results.pyc
    -rw-r--r--  1 qgis qgis 1.9K 2011-07-07 13:41 ui_results.ui

Notice the\  ``__init__.py`` \file. If you opened this file and looked at its guts, then you'd see high-level plugin descriptions such as names and verions numbers::

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

Also notice the resource files associated with this project below. Remember that the\  ``.qrc`` \file has to be compiled into a python module. Here's all of those files::

    -rw-r--r--  1 qgis qgis  23K 2011-07-07 13:41 resources.py
    -rw-r--r--  1 qgis qgis 6.1K 2011-07-07 13:41 resources.pyc
    -rw-r--r--  1 qgis qgis  143 2011-07-07 13:41 resources.qrc

The\  ``resources.py`` \and\  ``resources.pyc`` \are the compiled version of\  ``resources.qrc`` \.

With that said, it's probably a good guess that anything else with a\  ``.py`` \extension in this directory that we didn't talk about is related to the main plugin logic. There also seems to be some documents and images that we don't need to be concerned about at this point.

----------------------------

Installing QGIS Plugins
------------------------------

So how did the\  ``pluginbuilder`` \plugin get installed? How did it get in this directory? 

Let's review how we install Python plugins breifly.

\  **1.** \On the menu bar of QGIS click the\  ``Plugins > Fetch Python Plugins`` \item:

.. image:: ../_static/plugins_menu_click_1.png
    :scale: 100%
    :align: center

\  **2.** \A new dialog shows up with a list of available Python plugins for install. The tutorial authors have already setup QGIS to fetch 3rd-party plugins. If the tutorial authors had not done this there would be less plugins listed here. Click on the\  ``Repository`` \tab. This lists all the plugin repositories that are being searched for plugins. At the very bottom is a\  ``3rd Party Repositories`` \button. Click this button and QGSI will begin searching 3rd-party repositories for plugins: 

.. image:: ../_static/add_3rd_partyplugins_new.png
    :scale: 100%
    :align: center

\  **3.** \Now go to the\  ``Plugins`` \tab. The plugins for each repository show up here. Choose a plugin to download. I chose to install the osmpoly_export plugin:

.. image:: ../_static/qigs_install_osm_plugin.png
    :scale: 100%
    :align: center

\  **4.** \In the bash shell or folder browser navigate to\  ``/home/qgis/.qgis/python/plugins`` \. The plugin you chose to install should now be located here::

    $ cd /home/qgis/.qgis/python/plugins/
    $ ls -lah
    total 16K
    drwxr-xr-x 4 qgis qgis 4.0K 2011-08-20 12:26 .
    drwxr-xr-x 4 qgis qgis 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x 2 qgis qgis 4.0K 2011-08-20 12:26 osmpoly_export
    drwxr-xr-x 3 qgis qgis 4.0K 2011-07-07 13:41 pluginbuilder

\  **5.** \To turn any plugin on or off you can manage it by clicking\  ``Plugins > Manage Plugins`` \. The QGIS Plugin Manager dialog will launch with checkboxes next to the plugin you want to turn on or off:

.. image:: ../_static/plugin_manager_console.png
    :scale: 100%
    :align: center

 
----------------------------

Building Our First Plugin with 'Plugin Builder'
------------------------------------------------

Now it's time to get our feet wet by building our first plugin using\  **Plugin Builder** \to help us.

\  **1.** \On the QGIS menu bar click on the\  ``Plugin Builder`` \icon to launch the plugin:

.. image:: ../_static/plugin_builder_click1.png
    :scale: 100%
    :align: center

\  **2.** \The main Plugin Builder dialog will appear. This is where we fill out our basic configuration information that Plugin Builder uses to create the template files. We will then modify the template files to build out our plugin. All the fields in the dialog below are required. Fill these fields out like the picture shows. Then click the\  ``Ok`` \button.:

.. image:: ../_static/plugin_builder_main_dialog.png 
    :scale: 100%
    :align: center

\  **3.** \A file dialog will open. Create a\ ``workspace`` \folder inside your\  ``/home/qgis/`` \directory. Save your plugin project by selecting the\  ``workspace`` \directory in the file dialog:

.. image:: ../_static/plugin_builder_save_dir.png 
    :scale: 100%
    :align: center

\  **4.** \If everything went well, Plugin Builder will display a final dialog that shows us the next steps to customize our plugin project. Don't worry about folowing these because we will be detailing the exact same steps.

.. image:: ../_static/plugin_builder_feedback.png 
    :scale: 100%
    :align: center

\  **5.** \Now change into the workspace directory of your project\  ``/home/qgis/workspace/vector_selectbypoint`` \and list out the contents::

    $ cd workspace/vector_selectbypoint/
    $ ls -lah
    total 36K
    drwxr-xr-x 2 qgis qgis 4.0K 2011-08-20 13:21 .
    drwxr-xr-x 3 qgis qgis 4.0K 2011-08-20 17:34 ..
    -rw-r--r-- 1 qgis qgis 1.1K 2011-08-20 13:21 icon.png
    -rw-r--r-- 1 qgis qgis 1.6K 2011-08-20 13:21 __init__.py
    -rw-r--r-- 1 qgis qgis 1.9K 2011-08-20 13:21 Makefile
    -rw-r--r-- 1 qgis qgis  116 2011-08-20 13:21 resources.qrc
    -rw-r--r-- 1 qgis qgis 1.5K 2011-08-20 13:21 ui_vector_selectbypoint.ui
    -rw-r--r-- 1 qgis qgis 1.5K 2011-08-20 13:21 vector_selectbypointdialog.py
    -rw-r--r-- 1 qgis qgis 2.6K 2011-08-20 13:21 vector_selectbypoint.py


Notice that we have a single\  ``.ui`` \file and\  ``.qrc`` \file but that they haven't been compiled yet into Python modules. Let's compile these an take a quick look at what our plugin looks like so far inside QGIS.

\  **6.** \Luckily we have a\  ``Makefile`` \in this directory that we can use to compile both files easily. From inside the directory\  ``vector_selectbypoint`` \run the following command and it will print out two statements::

    $ make
    pyuic4 -o ui_vector_selectbypoint.py ui_vector_selectbypoint.ui
    pyrcc4 -o resources.py  resources.qrc

Those two statements are the commands we need to compile the appropriate resources and GUI files. We can either run these individually or just run the\  ``Makefile`` \to start them at the same time. Every time you make changes to the\  ``resources.qrc`` \or the\  ``ui_vector_selectbypoint.ui`` \file you will need to recompile.

\  **7.** \Now relist the contents of your directory and you will see more Python modules that were created. The important ones are these Python modules::
    
    $ ls -lah
    ... # MORE FILES WERE LISTED HERE
    -rw-r--r-- 1 qgis qgis 5.4K 2011-08-20 17:42 resources.py
    -rw-r--r-- 1 qgis qgis 1.4K 2011-08-20 17:42 ui_vector_selectbypoint.py
    ... # MORE FILES WERE LISTED HERE

\  **8.** \QGIS will now be able to read the files in our project and create an appropriate button on the menu bar. However, for QGIS to notice our new plugin we will need to put the our plugin folder inside of the\  ``/home/qgis/.qgis/python/plugins`` \directory. Instead of copying all our files there let's make a symbolic link (a shortcut) from our\  ``/home/qgis/workspace/vector_selectbypoing/`` \folder to the\  ``home/qgis/.qgis/python/plugings`` \folder. This way QGIS will notice our plugin project but the files are actually still located in our workspace folder for us to edit::

     $ ln -s /home/qgis/workspace/vector_selectbypoint/ /home/qgis/.qgis/python/plugins/

\  **9.** \If we change directories to\  ``/home/qgis/.qgis/python/plugins`` \and list it's contents we should see\  ``vector_selectbypoint`` \pointing to our workspace folder::

    $ cd /home/qgis/.qgis/python/plugins
    $ ls -lah
    total 16K
    drwxr-xr-x 4 qgis qgis 4.0K 2011-08-20 17:58 .
    drwxr-xr-x 4 qgis qgis 4.0K 2011-07-07 13:41 ..
    drwxr-xr-x 2 qgis qgis 4.0K 2011-08-20 12:26 osmpoly_export
    drwxr-xr-x 3 qgis qgis 4.0K 2011-07-07 13:41 pluginbuilder
    lrwxrwxrwx 1 qgis qgis   42 2011-08-20 17:58 vector_selectbypoint -> /home/qgis/workspace/vector_selectbypoint/

\  **10.** \Go back to QGIS and add the plugin to QGIS using the plugin manager\  ``Plugins > Manage Plugins`` \. When the QGIS Plugin Manager pops up start typing\  ``Select_`` \into the filter bar at top and our plugin will come up. Check the box to the left of our plugin. Then click the\  ``OK`` \button:

.. image:: ../_static/plugin_builder_adding2QGIS.png
    :scale: 100%
    :align: center

\  **11.** \You might notice that an icon has been added to the menu right next to our Plugin Builder command icon. Click this item:

.. image:: ../_static/click_vector_selectbypoint_tool.png
    :scale: 100%
    :align: center

\  **12.** \If everything went well, you will see an empty dialog with an\  ``OK`` \and\  ``Cancel`` \button. As you can see the Plugin Builder doesn't give us anything off-the-shelf that is useful. We have to customize it. But at least it works (yah!):

.. image:: ../_static/vector_selectbypoint_firstview.png
    :scale: 100%
    :align: center

-------------------------------------

Extending the Plugin Builder Templates
-----------------------------------------  




Examples
--------

