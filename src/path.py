class Path:
    def __init__(self, map_size, map):
        self.__output_data = {"length": 0, "path": [], "drop": 0}
        self.__map_size = map_size
        self.__map = map
        
    def get_path(self) -> dict:      
        longest_path = []
        m, n = self.__map_size
        max_drop = float('-inf')
        
        for i in range(m):
            for j in range(n):
                path = self.deep_first_search(i, j, [])
                steep = path[0] - path[-1]
                if len(path) >= len(longest_path):
                    if steep > max_drop:
                        longest_path = path
                        max_drop = steep
        
        self.__output_data["length"] = len(longest_path)
        self.__output_data["path"] = longest_path
        self.__output_data["drop"] = max_drop
        return self.__output_data 
    
    def deep_first_search(self, i: int, j: int, path: list) -> list:        
        # First check to see if cell is out of bounds
        cell_out_of_bounds = i >= self.__map_size[0] or j >= self.__map_size[1] \
                             or i < 0 or j < 0
        
        # Check if it's not decreasing
        not_decreasing = cell_out_of_bounds or \
                        (path and self.__map[i][j] >= path[-1])
                        
        if not_decreasing:
            return path
        
        # Adding map[i, j] to the path and apply the  same logic recursively in all directions
        up = self.deep_first_search(i - 1, j, path + [self.__map[i][j]])
        down = self.deep_first_search(i + 1, j, path + [self.__map[i][j]])
        right = self.deep_first_search(i, j + 1, path + [self.__map[i][j]])
        left = self.deep_first_search(i, j - 1, path + [self.__map[i][j]])
        
        return max(up, down, right, left, key=len)