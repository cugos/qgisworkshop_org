==========
VirtualBox
==========
We use a VirtualBox vdi disk image for this tutorial. Our VM has
the following software on it:

- Ubuntu 10.04 (minimal install)
- FireFox for viewing web content
- QT and PyQT development packages (from apt)
- QGIS built from SVN (Trunk on 07/01/11)

The base size for the disk image is:

- 3.1 GB uncompressed
- 1.1 GB compressed

The vdi can be downloaded from:
http://www.qgisworkshop.org/dl/qgis-foss4g11-1004.vdi.zip

To install the image:

- Install and start VirtualBox on the host system
- Create a new machine, using Linux - Ubuntu (32 bit) as the base type
- DO NOT create a new disk, instead select the supplied vdi as the disk
- Walk through the remainder of the setup 
- Boot

The system as one default user (with sudo privs):
User: qgis
Password: qgis

Have FUN!

================
QGIS from source
================
QGIS has been installed from the qgis users home directory.  If 
you open a terminal you will see a qgis-trunk directory.  To update 
the build you can::

  cd qgis-trunk
  svn up
  cd build
  make
  sudo make install


