import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\youngsang\data\data\geoportal.gdb"
outPath = env.workspace
arcpy.CreateFeatureclass_management(out_path = outPath, out_name = "newFC", geometry_type = "Point")