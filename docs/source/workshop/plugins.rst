=======
Plugins
=======

Plugin architecture
---------------------

QGIS Python plugins (fyi: you can also write plugins in C++) are really just a set of Python modules. We'll save the details for the\  **Examples** \section below, but here's a high-level overview:
    - There's a file that describes your Form (GUI)
    - a file that gives high level configuration information about your plugin
    - a file describing the resources your plugin will use
    - and finally, the meat-and-potatoes of the plugin is the file that that does the actual functional work of talking to your resources and GUI and whatever else.

Examples
--------

