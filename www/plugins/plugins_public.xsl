<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/plugins">

<html>
<head>
<title>FOSS4G 2011 Workshop Python Qgis Plugins</title>
<!--link href="xsl.css" rel="stylesheet" type="text/css" /-->

<style>
body  { 
   font-family:Verdana, Arial, Helvetica, sans-serif;
width: 50em;
 }

div.plugin { 
 background-color:#FFFFDF;
 border:1px solid #8FDF8F;
 clear:both;
 display:block;
 padding:0 0 0.5em;
 margin:1em;
}

div.head { 
  background-color:#FFFFAF;
  border-bottom-width:0;
  color:#FFF;
  display:block;
  font-size:110%;
  font-weight:bold;
  margin:0;
  padding:0.3em 1em;
}

div.description{ 
  display: block;
  float:none;
  margin:0;
  text-align: left;
  padding:0.2em 0.5em 0.4em;
  color: black;
  font-size:100%;
  font-weight:normal;
 }

div.download, div.author, div.experimental{ 
  font-size: 80%;
  padding: 0em 0em 0em 1em;
 }
</style>

</head>
<body>

<h1>FOSS4G 2011 Workshop PyQgis Plugins</h1>
<xsl:for-each select="/plugins/pyqgis_plugin">
<div class="plugin">
<div class="head">
<xsl:element name="a">
<xsl:attribute name="href">
<xsl:value-of select="homepage" />
</xsl:attribute>
<xsl:value-of select="@name" /> : <xsl:value-of select="@version" />
</xsl:element>
</div>
<div class="description">
<xsl:value-of select="description" />
</div>

<div class="download">
Download:
<xsl:element name="a">
 <xsl:attribute name="href">
  <xsl:value-of select="download_url" />
 </xsl:attribute>
 <xsl:value-of select="file_name" />
</xsl:element>
</div>
<div class="author">
Author: <xsl:value-of select="author_name" />
</div>
<div class="experimental">
Experimental: <xsl:value-of select="experimental" />
</div>

</div>
</xsl:for-each>


</body>
</html>

</xsl:template>

</xsl:stylesheet>
