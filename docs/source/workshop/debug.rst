
===================
Debugging Plugins
===================

Python console in QGIS
--------------------------
As we have been doing throughout this workshop, debugging via the python console is always available.

Using the PyQT debug hook
----------------------------
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

Pdb (like other debugging tools) also has command-line options that enhance the debugging experience. We'll go through some of the most popular commands below. For a full list check out the\  `official documentation <http://docs.python.org/library/pdb.html>`_ \.


\  **1.** \Once\  ``set_trace()`` \gets hit and throws us into a Pdb session we can see where we are in our code execution with the command\  ``list`` \.::

    (Pdb) list
     74         # run method that performs all the real work
     75         def run(self):
     76             pyqtRemoveInputHook()
     77             pdb.set_trace()
     78             # show the dialog
     79  ->         self.dlg.show()
     80             result = self.dlg.exec_()
     81             # See if OK was pressed
     82             if result == 1:
     83                 # do something useful (delete the line containing pass and
     84                 # substitute with your code

Notice the cute little arrow\  ``->`` \. This command without arguments returns 11 lines, with the currently executing line in the middle.


\  **2.** \The\  ``list`` \command is pretty dynamic, which means we can list out any portion of code using two numeric line-number arguments. Here's a couple variations on this command::

    (Pdb) list 60
     55             #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )
     56     
     57         def unload(self):
     58             # Remove the plugin menu item and icon
     59             self.iface.removePluginMenu("&a tool that displays raster values on-the-fly",self.action)
     60             self.iface.removeToolBarIcon(self.action)
     61     
     62         def handleXY(self, point):
     63             #QMessageBox.information( self.iface.mainWindow(), "Info", str(point.x()) + "," + str(point.y()) )
     64             self.dlg.clearTextBrowser()
     65             self.cLayer = self.canvas.currentLayer()
    (Pdb) list 60, 75
     60             self.iface.removeToolBarIcon(self.action)
     61     
     62         def handleXY(self, point):
     63             #QMessageBox.information( self.iface.mainWindow(), "Info", str(point.x()) + "," + str(point.y()) )
     64             self.dlg.clearTextBrowser()
     65             self.cLayer = self.canvas.currentLayer()
     66             if self.cLayer:
     67                 if self.cLayer.type() == 1:
     68                     success, data = self.cLayer.identify(point)
     69                     final = "" 
     70                     for key,value in data.items():
     71                         final += str(key) + " > " + str(value) + "\n"
     72                     self.dlg.setTextBrowser(final) 
     73     
     74         # run method that performs all the real work
     75         def run(self):

A single numberic arguments prints out the line we wanted buffered by 5 lines before and after. Two arguments prints us a the range of code for those line numbers.

\  **3.** \We can also set more breakpoints once we are in Pdb. We can use the\  ``break`` \command or just\  ``b`` \for shorthand plus a numberic argument that designates what line number we want to put a breakpoint on::

    (Pdb) b 64
    Breakpoint 1 at /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py:64

\  **4.** \If we want to see how many current breakpoints already exists we just use the\  ``break`` \command with no arguments. Notice that the 'Num' value is the key identifer for the breakpoint. We can use this ID if we want to pass this breakpoint as argument to another command (as we'll see)::

    (Pdb) b
    Num Type         Disp Enb   Where
    1   breakpoint   keep yes   at /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py:64

\  **5.** \Now that I've set a new breakpoint, I'll want to continue my code execute until I hit it. I can continue execution with the\  ``c`` \or\  ``continue`` \command.::

    (Pdb) c
    > /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py(64)handleXY()
    -> self.dlg.clearTextBrowser()
    (Pdb) list
     59             self.iface.removePluginMenu("&a tool that displays raster values on-the-fly",self.action)
     60             self.iface.removeToolBarIcon(self.action)
     61     
     62         def handleXY(self, point):
     63             #QMessageBox.information( self.iface.mainWindow(), "Info", str(point.x()) + "," + str(point.y()) )
     64 B->         self.dlg.clearTextBrowser()
     65             self.cLayer = self.canvas.currentLayer()
     66             if self.cLayer:
     67                 if self.cLayer.type() == 1:
     68                     success, data = self.cLayer.identify(point)
     69                     final = "" 

Notice that when i listed out where the execution stopped I got a pretty\  ``B->`` \to show it was a breakpoint. 

\  **6.** \We can traverse our code line-by-line with two commands:\  ``step`` \and\  ``next`` \. Though\  ``step`` \will walk into every function (even Python standard functions) and\  ``next`` \will just execute them and move to the next line. So be sure you understand your outcome. Assuming my execution was on the last breakpoint above,\  ``next`` \should bring me to line 65::

    (Pdb) n
    > /home/gcorradini/.qgis/python/plugins/rastervaluedisplay/rastervaluedisplay.py(65)handleXY()
    -> self.cLayer = self.canvas.currentLayer()
    (Pdb) list
     60             self.iface.removeToolBarIcon(self.action)
     61     
     62         def handleXY(self, point):
     63             #QMessageBox.information( self.iface.mainWindow(), "Info", str(point.x()) + "," + str(point.y()) )
     64 B           self.dlg.clearTextBrowser()
     65  ->         self.cLayer = self.canvas.currentLayer()
     66             if self.cLayer:
     67                 if self.cLayer.type() == 1:
     68                     success, data = self.cLayer.identify(point)
     69                     final = "" 
     70                     for key,value in data.items():


Yep, that worked (Yah!)

\  **7.** \Finally, we can remove breakpoints with the command\  ``clear`` \or\  ``cl`` \for short. We then give a numeric line-number argument where a breakpoint exists::

    (Pdb) cl 1
    Deleted breakpoint 1



