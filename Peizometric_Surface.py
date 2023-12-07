import arcpy

folder_path= r'C:\\Users\\Grady\\Desktop\\GISProject'
gdb_name='Peizometric_Surface.gdb'
gdb_path=folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path,gdb_name)

#plots xy data from csv
arcpy.management.XYTableToPoint(r"C:\\Users\\Grady\\Desktop\\GISProject\\ogalla2022_data.csv", 
r"C:\\Users\\Grady\\Desktop\\GISProject\\ogalla2022_data.csv", 
"LongitudeDD",
 "LatitudeDD", 
 None, 
 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision')

print("xy data successfully plotted")

out_surface_raster = arcpy.sa.TopoToRaster("ogalla2022_data.shp WaterEleva PointElevation", 0.0122555588, 
'-103.064723 31.8636111000001 -100.0008333 36.4997220000001 GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
, 20, None, None, "ENFORCE", "CONTOUR", 20, None, 1, 0, 2.5, 100, None, None, None, None, None, None, None, None); out_surface_raster.save(r"C:\\Users\\Grady\Desktop\\GISProject\\Peizometric_surface.gdb\\Peizometric_Surface")

print("peixometric surface successfully generated")

  