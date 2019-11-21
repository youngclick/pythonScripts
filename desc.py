#describe function
#10/22
import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\youngsang\data\data\geoportal.gdb"
desc = arcpy.Describe("School")
print "Shape type: " + desc.shapeType
print "hasM: " + str(desc.hasM)
print "Feature type: " + desc.featureType
print desc.shapeFieldName
print desc.extent.XMin