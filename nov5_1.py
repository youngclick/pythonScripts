import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\youngsang\data1\data1\USA.gdb"
env.overwriteOutput = True

fc = "us_cities"
print "worked"

rows = arcpy.SearchCursor(fc)
row = rows.next()

while row:
    print row.NAME
    row = rows.next()