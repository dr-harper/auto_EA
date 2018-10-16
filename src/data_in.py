"""Define class for importing data"""

import operator
import geopandas


class InputFiles:
	"""Takes a list of file names and returns only those with required extensions

	Args:
		files -- a list of filenames
	"""
	def __init__(self, files):
		self.files = files

	files = property(operator.attrgetter('_files'))

	@files.setter
	def files(self, f):
		"""Checks files is a list and raises exception if not"""
		if not isinstance(f, list):
			raise Exception("filenames must be a list")
		self._files = f

	def is_shapefile(self):
		"""Takes a list of files and returns a list containing those with extension .shp

		Returns:
			shp_files -- a list of all file names with .shp extension
		"""
		shp_files = []
		for f in self.files:
			if isinstance(f, str):
				if f[-4:] == '.shp':
					shp_files.append(f)

		return shp_files

	def is_raster(self):
		"""Takes a list of files and returns a list containing those with extension .tiff

		Returns:
			rst_files -- a list of all file names with .tiff extension """
		rst_files = []
		for f in self.files:
			if f.lower.endswith('.tiff'):
				rst_files.append(f)

		return rst_files


class AggregateData:
	"""All functions for pulling multiple data sources together

	Args:
		geodatafames -- a dictionary of geodataframes
	"""
	def __init__(self, geodataframes):
		self.geodataframes = geodataframes

	# geodataframes = property(operator.attrgetter('_geodataframes'))
	#
	# @geodataframes.setter
	# def files(self, gdf):
	# 	"""Checks files is a list and raises exception if not"""
	# 	if not isinstance(gdf, dict):
	# 		raise Exception("geodataframes must be a dict")
	# 	self._geodataframes = f

	def merge_shapes(self):
		"""Iteratively Merge given geodataframes to form single dataframe

		Returns:
			merged -- a single geodataframe formed by the union of all
			geodataframes passed to AggregateData instance.
		"""
		# TODO: add checks for empty files and files with no polygons
		counter = 0
		for ds in self.geodataframes.keys():
			print(ds)
			if counter == 0:
				merged = self.geodataframes[ds]
			else:
				merged = geopandas.overlay(merged, self.geodataframes[ds], how='union')
			counter += 1
		return merged
