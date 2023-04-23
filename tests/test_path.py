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
        print('--------------- Testing 4x4 map-----------------------')
        self.map_path = './data/4x4.txt'
        map_size, map = self.utils.parse_data(self.map_path)
        path = Path(map_size, map).get_path()
        print("output ======> ")
        print(f'length: {path["length"]}\npath: {path["path"]}\ndrop: {path["drop"]}')
        self.assertEqual(path, {"length": 5, "path": [9, 5, 3, 2, 1], "drop": 8})
    
    def test_last_map(self):
        print('--------------- Testing 1000x1000 map-----------------------')
        self.map_path = './data/map.txt'
        map_size, map = self.utils.parse_data(self.map_path)
        path = Path(map_size, map).get_path()
        print("output ======> ")
        print(f'length: {path["length"]}\npath: {path["path"]}\ndrop: {path["drop"]}')