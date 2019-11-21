import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\youngsang"
env.overwriteOutput = True

fc = "us_major_cities.shp"
total = 0
counts = 0
with arcpy.da.SearchCursor(fc, ("NAME","POPULATION")) as cursor:
    for row in cursor:
        total += row[1]
        counts += 1.0

print "average population is ", (total/counts) 

##for row in rows:
##    print row.getValue(fieldName0)
##    

##while row:
##    print row.getValue(fieldName0), row.getValue(fieldName1)
##    row = rows.next()