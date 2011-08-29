
===================
Debugging Plugins
===================

Python console in QGIS
----------------------
As we have been doing throughout this workshop, debugging via the python console is always available.

Using the PyQT debug hook
--------------------
When trying to debug python plugins, one of the best methods is to use \ `PDB <http://docs.python.org/library/pdb.html>`_ \.  When using \ `PDB <http://docs.python.org/library/pdb.html>`_ \ you need to add the following code to your plugin python file(s)::

    from PyQt4 import QtCore
    import pdb
    ...
    QtCore.pyqtRemoveInputHook()
    pdb.set_trace()

You will need to add the pdb.set_trace() where you would like to set a break point in your code.  You then run QGIS from the command line and when the set_trace call is hit, you will be dropped into a PDB prompt at the command line.  At this point you will have a "GDB" like debug environment where you can view and set variables as well as walk through code::

    > /home/qgis/.qgis/python/plugins/DockableMirrorMap/mirrorMap.py(183)addLayer()
    -> prevFlag = self.canvas.renderFlag()
    (Pdb) bt
    > /home/qgis/.qgis/python/plugins/DockableMirrorMap/mirrorMap.py(183)addLayer()
    -> prevFlag = self.canvas.renderFlag()
    (Pdb) print self
    <DockableMirrorMap.mirrorMap.MirrorMap object at 0xabfa5ec>
    (Pdb) print self.iface.mainWindow().windowTitle()
    Quantum GIS 1.7.0-Wroclaw
    (Pdb) aLayer = self.iface.activeLayer()
    (Pdb) aLayer
    <qgis.core.QgsVectorLayer object at 0xabfa6ac>
    (Pdb) aLayer.name()
    PyQt4.QtCore.QString(u'50m_admin_0_boundary_breakaway_disputed_areas')
    (Pdb) 
    

Pdb Commands and Tricks
---------------------------



