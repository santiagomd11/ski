import numpy as np

class Path:
    def __init__(self, map_size, map):
        self.__output_data = {}
        self.__map_size = map_size
        self.__map = map
        
    def get_path(self) -> dict:      
        print(self.__map)
        return self.__output_data 