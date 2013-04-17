#!/usr/local/bin/python
# =========================================================================================
# Script : createFindIndexes.py
# -----------------------------------------------------------------------------------------
# Purpose : This script creates a an xml of unique feature class feature names to be used
#           with RegGSS Finds.
# -----------------------------------------------------------------------------------------
# Suppliment Info:
# -----------------------------------------------------------------------------------------
# Supervisor : Juan Tobar, Regulation SFWMD, (561)682-6687
# Create date: 9 April 2013
#------------------------------------------------------------------------------------------

# Import system modules
import sys
import string
import os
#import shutil
#import pyodbc
import arcpy
#import time

def createFindIndexes():
    from xml.etree import ElementTree
    from xml.etree.ElementTree import Element
    from xml.etree.ElementTree import SubElement

    # <configuration/>
    configuration = Element( 'configuration' )

    # <configuration><feature_class/>
    feature_class = SubElement( configuration, 'AHED.HYDROEDGE' )

    valueList = []
    rows = arcpy.SearchCursor("Database Connections/gisuser@ghydp_ghydpsde.sde/AHED.HYDROEDGE", "", "", "NAME")
    for row in rows:
        strValue = str(row.getValue("NAME"))
        if strValue != 'None' and strValue != "<Null>" and strValue != ' ' and strValue != '':
            valueList.append(strValue)    

    del rows
    del row
    
    uniqueSet = set(valueList)
    uniqueList = list(uniqueSet)
    uniqueList.sort()

    for s in uniqueList:
        # <configuration><feature_class><feature_name/>
        SubElement( feature_class, 'AHED.HYDROEDGE', feature_name='%s' %s)

    output_file = open( '//ad.sfwmd.gov/dfsroot/data/err_gis/scratch/jtobar/ahed_hydroedge_index.xml', 'w' )
    output_file.write( '<?xml version="1.0"?>' )
    output_file.write( ElementTree.tostring( configuration ) )
    output_file.close()
    
try:
    createFindIndexes()

    
except NameError, e:
    print e
    
