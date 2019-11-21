import arcpy
fc = r"H:\PythonGIS\youngsang\us_major_cities.shp"

where = """"CAPITAL" = 'NEW'"""
where1 = '"CAPITAL"'+" = '" + "State1'"
print where1
##with arcpy.da.UpdateCursor(fc, ("CAPITAL",),where_clause = where1) as cursor:
##    for row in cursor:
##        row[0] = "State"
##        cursor.updateRow(row)
print "NEW"
with arcpy.da.SearchCursor(fc, ["SHAPE@X","OID@"]) as cursor:
    for row in cursor:
        print row[0], row[1]