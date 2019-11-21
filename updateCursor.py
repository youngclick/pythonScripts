import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\youngsang"
env.overwriteOutput = True

fc = "us_major_cities.shp"
where = "CAPITAL" == 'State'
print where
with arcpy.da.UpdateCursor(fc, ("CAPITAL",),where) as cursor:
    for row in cursor:
        row[0] = "capital"

