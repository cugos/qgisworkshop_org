###################
# REQUIREMENTS
###################

We tested out this Virtual Box Ubuntu 10.04 image on Virtual Box version 4.0.10. We would like Virtual Box 4.x installed on the workshop computer.

###################
# INSTALLATION
###################

These instructions specify how to extract and import the Virtual Box VDI contained inside qgis-foss4g11-1004.vdi.zip

## EXTRACT

 unzip qgis-foss4g11-1004.vdi.zip

## CREATE MACHINE

 start Virtual Box 4.0.10

 Create a new virtual machine by clicking "New" in the top left-hand menu or typing <Ctrl+N>

 Click Next

 The "VM Name and OS Type" dialog opens. Please name the virutal machine "PYQGIS_PLUGINS"

 Then select Linux in the "Operating System" drop down menu and select Ubuntu (32bit) in the "Version" drop down

 Click Next
 
 In the "Memory" dialog change the default setting to 1GB 

 Click Next

 In the "Virtual Disk" dialog please select "Use existing hard disk" and navigate to the unzipped qgis-foss4g11-1004.vdi

 Click Next

 Click Finish

## SETUP AND CONFIG

 We want to create a shared folder between the host operating system and the guest operating system.

 Before starting the "PYQGIS_PLUGINS" machine create a folder called "vm_shared" on the C:\\ drive -- "C:\\vm_shared"

 Make sure the "vm_shared" directory has read-write-execute permissions for the "user" and "group"

 Now right-click on the "PYQGIS_PLUGINS" machine in the left window and click "Settings"

 Click on the "Shared Folders" node at the bottom-left

 Add a new shared folder definition by clicking the folder-plus icon in the top right just right of the column "Access"

 In the "Folder Path" drop down click "Other" and navigate to "C:\\" directory. Select "C:\\vm_shared" and click "Open"

 Then in the "Folder Name" text box make sure it says "vm_shared" ( after last step it should automatically appear )

 Check the checkbox next to "Auto-mount" and  **DO NOT** check the "Read-only" check box

 Click "OK"

 Click "OK" again

 Then start the virtual "PYQGIS_PLUGINS" machine

## TESTING INSTALL

 Test internet connectivity by clicking on the "FireFox" icon on the top menu bar

 The default homepage should jump to http://www.qgisworkshop.org/html/

 Test shared-drive by navigating to /home/qgis on the "PYQGIS_PLUGIN" virtual machine

 If everything was setup correclty you should be able to navigate into the "shared_drive" directory inside /home/qgis

 Then on the "PYQGIS_PLUGIN" virtual machine navigate into "shared_drive" directory and create a blank text file 

 On the host operating system (not in the virtual machine) navigate to "C:\\vm_shared" to make sure the text file you created appears there also


## SHUTDOWN

 When turning off the machine please select "Shutdown" instead of "Power off" option in the menu


## END
Thanks bunches ;-)
 

 
 

  
  






