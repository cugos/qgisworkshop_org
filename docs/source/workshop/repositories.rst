
=====================
Plugin Repositories
=====================

Official repositories
---------------------
When searching for plugins to install or use as examples, the official \ `QGIS Plugin repository <http://plugins.qgis.org/plugins/>`_ \ is the best place to start.  An older version of the user contributed plugin repository is located \ `here <http://pyqgis.org/repo/contributed>`_ \.  While the community of plugin developers is growing, so has been the process for plugin develpment.  Historically developers were relagated to maintaining thier own repositories, and many still exist today.

Publicly available remote repositories
-------------------
There are also a number of hard coded public repositories that are maintained by 3rd parties that are also available.  In the Fetch Python Plugins dialog, under the Repositories tab you can select to "Add 3rd party repositories".  With this option you will get a well known list of public repositories, but these are not tracked or screened by the QGIS project... so use at your own risk.

Your own private repository
--------------------
If you wish to create your own private repository, it is as simple as creating a web accessable (can be on local machine) XML file properly describing to QGIS where to download the plugin.  The following is an example of the XML structure needed::

    <?xml version = '1.0' encoding = 'UTF-8'?>
    <?xml-stylesheet type='text/xsl' href='/plugins.xsl' ?>
    <plugins>
      <pyqgis_plugin name='Plugin Installer' version='1.1'>
        <description>The recent Python Plugin Installer</description>
        <version>1.1</version>
        <qgis_minimum_version>1.0</qgis_minimum_version>
        <homepage>http://www.bwj.aster.net.pl/qgis/</homepage>
        <file_name>plugin_installer.zip</file_name>
        <author_name>Borys Jurgiel</author_name>
        <download_url>http://spatialserver.net/pyqgis_1.0/plugins/plugin_installer.zip</download_url>
        <uploaded_by>borysiasty</uploaded_by>
        <create_date>2008-12-18</create_date>
        <update_date>2010-10-31</update_date>    
      </pyqgis_plugin>
    </plugins>


Packaging
---------
To package you need to finalize all of your code and UI files, and then zip the package up to be distributed.  QGIS expects the zip package to contain the directory structure that will be housed in the .qgis directory, so the following command on linuz systems will get you what you need::

    zip -9vr myPlugin.zip myPlugin/*

