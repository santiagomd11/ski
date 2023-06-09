class Utils:
    def parse_data(self, map_path: str) -> list:
        size = []
        output_array = []
        with open(map_path, 'r') as f:
            for line_number, line in enumerate(f.readlines()):
                line = list(map(int, line.split()))
                if line_number == 0:
                    size.extend(line)
                else:
                    output_array.append(line)
        return (size, output_array)