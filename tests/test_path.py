import unittest
from src.path import Path

class PathTestCase(unittest.TestCase):
    def setUp(self):
        self.path = Path()
        self.map = ''
    
    def tearDown(self):
        self.map = ''
    
    def test_path_first_map(self):
        self.map = './data/4x4.txt'
        path = self.path.getPath(self.map)
        self.assertEqual(path, {"length:": 5, "path": [9, 5, 3, 2, 1], "drop": 8})