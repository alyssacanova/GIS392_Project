##### Ogallala Aquifer Water Quality Analysis #####
###                 Alyssa Canova               ###

## input is cleaned .csv file containing water quality parameter data obtained from the TWDB GWDB ##

import arcpy 

## Step 1. "XY Table to Point"

arcpy.management.XYTableToPoint(
    in_table=r"C:\Users\canov\OneDrive\Desktop\GIS_676\project\WaterQualityIndex.csv",
    out_feature_class=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\WaterQualityIndex_XYTableToPoint1",
    x_field="LongitudeDD",
    y_field="LatitudeDD",
    z_field=None,
    coordinate_system='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision'
)

## Step 2. "Empirical Bayesian Kriging" for each parameter

# Calcium
arcpy.ga.EmpiricalBayesianKriging(
    in_features="WaterQualityIndex_XYTableToPoint1",
    z_field="Calcium",
    out_ga_layer=None,
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\Calcium_interpolated",
    cell_size=0.0114444464000001,
    transformation_type="NONE",
    max_local_points=100,
    overlap_factor=1,
    number_semivariograms=100,
    search_neighborhood="NBRTYPE=StandardCircular RADIUS=1.34011549549716 ANGLE=0 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR",
    output_type="PREDICTION",
    quantile_value=0.5,
    threshold_type="EXCEED",
    probability_threshold=None,
    semivariogram_model_type="POWER"
)

# Chloride
arcpy.ga.EmpiricalBayesianKriging(
    in_features="WaterQualityIndex_XYTableToPoint1",
    z_field="Chloride",
    out_ga_layer=None,
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\Chloride_interpolated",
    cell_size=0.0114444464000001,
    transformation_type="NONE",
    max_local_points=100,
    overlap_factor=1,
    number_semivariograms=100,
    search_neighborhood="NBRTYPE=StandardCircular RADIUS=1.34011549549716 ANGLE=0 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR",
    output_type="PREDICTION",
    quantile_value=0.5,
    threshold_type="EXCEED",
    probability_threshold=None,
    semivariogram_model_type="POWER"
)

# pH
arcpy.ga.EmpiricalBayesianKriging(
    in_features="WaterQualityIndex_XYTableToPoint1",
    z_field="ph",
    out_ga_layer=None,
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\pH_interpolated",
    cell_size=0.0114444464000001,
    transformation_type="NONE",
    max_local_points=100,
    overlap_factor=1,
    number_semivariograms=100,
    search_neighborhood="NBRTYPE=StandardCircular RADIUS=1.34011549549716 ANGLE=0 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR",
    output_type="PREDICTION",
    quantile_value=0.5,
    threshold_type="EXCEED",
    probability_threshold=None,
    semivariogram_model_type="POWER"
)

# Total Hardness
arcpy.ga.EmpiricalBayesianKriging(
    in_features="WaterQualityIndex_XYTableToPoint1",
    z_field="TotalHardness",
    out_ga_layer=None,
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\TotalHardness_interpolated",
    cell_size=0.0114444464000001,
    transformation_type="NONE",
    max_local_points=100,
    overlap_factor=1,
    number_semivariograms=100,
    search_neighborhood="NBRTYPE=StandardCircular RADIUS=1.34011549549716 ANGLE=0 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR",
    output_type="PREDICTION",
    quantile_value=0.5,
    threshold_type="EXCEED",
    probability_threshold=None,
    semivariogram_model_type="POWER"
)

# Fluoride
arcpy.ga.EmpiricalBayesianKriging(
    in_features="WaterQualityIndex_XYTableToPoint1",
    z_field="Fluoride",
    out_ga_layer=None,
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\Fluoride_interpolated",
    cell_size=0.0114444464000001,
    transformation_type="NONE",
    max_local_points=100,
    overlap_factor=1,
    number_semivariograms=100,
    search_neighborhood="NBRTYPE=StandardCircular RADIUS=1.34011549549716 ANGLE=0 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR",
    output_type="PREDICTION",
    quantile_value=0.5,
    threshold_type="EXCEED",
    probability_threshold=None,
    semivariogram_model_type="POWER"
)

# Total Dissolved Solids (TDS)
arcpy.ga.EmpiricalBayesianKriging(
    in_features="WaterQualityIndex_XYTableToPoint1",
    z_field="TDS",
    out_ga_layer=None,
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\TDS_interpolated",
    cell_size=0.0114444464000001,
    transformation_type="NONE",
    max_local_points=100,
    overlap_factor=1,
    number_semivariograms=100,
    search_neighborhood="NBRTYPE=StandardCircular RADIUS=1.34011549549716 ANGLE=0 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR",
    output_type="PREDICTION",
    quantile_value=0.5,
    threshold_type="EXCEED",
    probability_threshold=None,
    semivariogram_model_type="POWER"
)

# Nitrate
arcpy.ga.EmpiricalBayesianKriging(
    in_features="WaterQualityIndex_XYTableToPoint1",
    z_field="Nitrate",
    out_ga_layer=None,
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\Nitrate_interpolated",
    cell_size=0.0114444464000001,
    transformation_type="NONE",
    max_local_points=100,
    overlap_factor=1,
    number_semivariograms=100,
    search_neighborhood="NBRTYPE=StandardCircular RADIUS=1.34011549549716 ANGLE=0 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR",
    output_type="PREDICTION",
    quantile_value=0.5,
    threshold_type="EXCEED",
    probability_threshold=None,
    semivariogram_model_type="POWER"
)

## Step 3. "Clip Raster" for each parameter

# Calcium
arcpy.management.Clip(
    in_raster="Calcium_interpolated",
    rectangle="-103.064743760914 31.7434204430459 -100.000071539421 36.50123809573",
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\Calcium_interpolated_clipped",
    in_template_dataset="Ogallala_boundary",
    nodata_value="3.4e+38",
    clipping_geometry="ClippingGeometry",
    maintain_clipping_extent="NO_MAINTAIN_EXTENT"
)

# Chloride 
arcpy.management.Clip(
    in_raster="Chloride_interpolated",
    rectangle="-103.064743760914 31.7434204430459 -100.000071539421 36.50123809573",
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\Chloride_interpolated_clipped",
    in_template_dataset="Ogallala_boundary",
    nodata_value="3.4e+38",
    clipping_geometry="ClippingGeometry",
    maintain_clipping_extent="NO_MAINTAIN_EXTENT"
)

# pH
arcpy.management.Clip(
    in_raster="pH_interpolated",
    rectangle="-103.064743760914 31.7434204430459 -100.000071539421 36.50123809573",
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\pH_interpolated_clipped",
    in_template_dataset="Ogallala_boundary",
    nodata_value="3.4e+38",
    clipping_geometry="ClippingGeometry",
    maintain_clipping_extent="NO_MAINTAIN_EXTENT"
)

# Total Hardness
arcpy.management.Clip(
    in_raster="TotalHardness_interpolated",
    rectangle="-103.064743760914 31.7434204430459 -100.000071539421 36.50123809573",
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\TotalHardness_interpolated_clipped",
    in_template_dataset="Ogallala_boundary",
    nodata_value="3.4e+38",
    clipping_geometry="ClippingGeometry",
    maintain_clipping_extent="NO_MAINTAIN_EXTENT"
)

# Fluoride
arcpy.management.Clip(
    in_raster="Fluoride_interpolated",
    rectangle="-103.064743760914 31.7434204430459 -100.000071539421 36.50123809573",
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\Fluroide_interpolated_clipped",
    in_template_dataset="Ogallala_boundary",
    nodata_value="3.4e+38",
    clipping_geometry="ClippingGeometry",
    maintain_clipping_extent="NO_MAINTAIN_EXTENT"
)

# TDS
arcpy.management.Clip(
    in_raster="TDS_interpolated",
    rectangle="-103.064743760914 31.7434204430459 -100.000071539421 36.50123809573",
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\TDS_interpolated_clipped",
    in_template_dataset="Ogallala_boundary",
    nodata_value="3.4e+38",
    clipping_geometry="ClippingGeometry",
    maintain_clipping_extent="NO_MAINTAIN_EXTENT"
)

# Nitrate
arcpy.management.Clip(
    in_raster="Nitrate_interpolated",
    rectangle="-103.064743760914 31.7434204430459 -100.000071539421 36.50123809573",
    out_raster=r"C:\Users\canov\OneDrive\Documents\ArcGIS\Projects\GIS_PiezometricSurface\GIS_PiezometricSurface.gdb\Nitrate_interpolated_clipped",
    in_template_dataset="Ogallala_boundary",
    nodata_value="3.4e+38",
    clipping_geometry="ClippingGeometry",
    maintain_clipping_extent="NO_MAINTAIN_EXTENT"
)

## Step 4. adjust symbology for each parameter 
    # completed in ArcGIS Pro

## Step 5. add "Qi" and "Wi" columns for each parameter
    # completed in ArcGIS Pro
    # "float"

# Step 6. add "WQI" column
    # completed in ArcGIS Pro

# Step 7. "Calculate Field" used to calculate Qi and Wi for each parameter 

# Qi:
    # Qi_parameter1 = (actual_value - ideal_value)/(standard_value - ideal_value) * 100

#Calcium
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Qi_Calcium",
    expression="(!Calcium!)/(75) * 100",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Chloride
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Qi_Chloride",
    expression="(!Chloride!)/(250) * 100",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# pH
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Qi_pH",
    expression="(!pH! - 7)/(1.5) * 100",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Total Hardness
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Qi_Hardness",
    expression="(!TotalHardness!)/(300) * 100",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Fluoride
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Qi_Fluoride",
    expression="(!Fluoride!)/(1) * 100",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# TDS 
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Qi_TDS",
    expression="(!TDS!)/(500) * 100",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Nitrate
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Qi_Nitrate",
    expression="(!Nitrate!)/(45) * 100",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Wi:
    # Wi_parameter1 = (1/standard_value)
    
#Calcium
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Wi_Calcium",
    expression="1/75",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Chloride
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Wi_Chloride",
    expression="1/250",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# pH
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Wi_pH",
    expression="1/8.5",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Total Hardness
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Qi_Hardness",
    expression="1/300",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Fluoride
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Wi_Fluroide",
    expression="1",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# TDS 
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Wi_TDS",
    expression="1/500",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Nitrate
arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="Wi_Nitrate",
    expression="1/45",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Step 8. "Calculate Field" used to calculate WQI
    # WQI = ∑ QiWi / ∑ Wi

arcpy.management.CalculateField(
    in_table="WaterQualityIndex_XYTableToPoint",
    field="WQI",
    expression="(!Qi_Calcium! * !Wi_Calcium! + !Qi_Chloride! * !Wi_Chloride! + !Qi_Fluoride! * !Wi_Fluroide! + !Qi_Hardness! * !Wi_Hardness! + !Qi_Nitrate! * !Wi_Nitrate! + !Qi_pH! * !Wi_pH! + !Qi_TDS! * !Wi_TDS!) / (!Wi_Calcium! + !Wi_Chloride! + !Wi_Fluroide! + !Wi_Hardness! + !Wi_Nitrate! + !Wi_pH! + !Wi_TDS!)",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)


