# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from vector_selectbypointdialog import vector_selectbypointDialog

class vector_selectbypoint:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/vector_selectbypoint/icon.png"), \
            "some text that appears in the menu", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&some text that appears in the menu", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&some text that appears in the menu",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # create and show the dialog
        dlg = vector_selectbypointDialog()
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass

