#!/usr/local/bin/python
# =========================================================================================
# Script : createFindIndexes.py
# -----------------------------------------------------------------------------------------
# Purpose : This script creates an xml of unique feature class feature names to be
#           loaded into the RegGSS - Find Canals (AHED) listbox.
# -----------------------------------------------------------------------------------------
# Supplemental Info:
# -----------------------------------------------------------------------------------------
# Supervisor : Juan Tobar, Regulation GIS, SFWMD
# Create date: 9 April 2013
#------------------------------------------------------------------------------------------

# Import system modules
import sys
import string
import os
import arcpy

def createFindIndexes():
    #XML Elements
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
        # remove junk feature names
        if strValue != 'None' and strValue != "<Null>" and strValue != ' ' and strValue != '':
            valueList.append(strValue)    

    del rows
    del row
    
    # set is used to create a unique list of values
    uniqueSet = set(valueList)
    # convert it back to a list so it can be sorted
    uniqueList = list(uniqueSet)
    uniqueList.sort()

    # iterate through the list constructing the SubElements
    for s in uniqueList:
        # <configuration><feature_class><feature_name/>
        SubElement( feature_class, 'AHED.HYDROEDGE', feature_name='%s' %s)

    # create the XML output
    output_file = open( '//ad.sfwmd.gov/dfsroot/data/err_gis/scratch/jtobar/ahed_hydroedge_index.xml', 'w' )
    # you have to add the xml version manually
    output_file.write( '<?xml version="1.0"?>' )
    # but the rest is automated
    output_file.write( ElementTree.tostring( configuration ) )
    output_file.close()
    
try:
    createFindIndexes()

    
except NameError, e:
    print e
    
