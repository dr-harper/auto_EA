import unittest
import data_in


class TestInputs(unittest.TestCase):
	def test_name_is_string(self):
		d = data_in.InputFiles.is_shapefile(['somestring'])
		self.assertIsInstance(d, str)


if __name__ == '__main__':
	unittest.main()
