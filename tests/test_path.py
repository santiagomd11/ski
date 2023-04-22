import unittest
from src.path import Path
from src.utils import Utils

class PathTestCase(unittest.TestCase):
    def setUp(self):
        self.utils = Utils()
        self.map_path = ''
    
    def tearDown(self):
        self.map_path = ''
    
    def test_path_first_map(self):
        self.map_path = './data/4x4.txt'
        map_size, map = self.utils.parse_data(self.map_path)
        path = Path(map_size, map).get_path()
        self.assertEqual(path, {"length:": 5, "path": [9, 5, 3, 2, 1], "drop": 8})