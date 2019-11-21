#Describe function second day
#Youngsang Kwon

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\youngsang\data\data\geoportal.gdb"
env.overwriteOutput = True

fc = "Fire"
desc = arcpy.Describe(fc)
print desc.shapeType
print desc.spatialReference.name
for field in desc.fields:
    print field.name, field.length

print arcpy.ListFeatureClasses()