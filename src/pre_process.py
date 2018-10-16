"""Prepare input data for analysis"""

import os
import data_in
import geopandas
import geoplot
import matplotlib.pyplot as plt

# Load data
path = "/Users/frejahunt/Documents/EA tool/auto_EA/testdata/"
files = os.listdir(path)

# Extracts the shapefiles from the list in the specified folder
files_in = data_in.InputFiles(files).is_shapefile()

# Import those files
data = {}
for f in files_in:
	data[f] = geopandas.GeoDataFrame.from_file(path + f)

# Flatten all datasets together
merged = data_in.AggregateData(data).merge_shapes()

# Check results
fig, ax = plt.subplots()
data['gis.osm_water_a_free_1.shp'].plot(ax=ax, edgecolor='black')
data['gis.osm_landuse_a_free_1.shp'].plot(ax=ax, edgecolor='green')
geoplot.polyplot(merged, ax=ax, edgecolor='red')
plt.show()


