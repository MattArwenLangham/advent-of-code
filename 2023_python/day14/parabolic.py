def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().split("\n")

movable = 'O'
immovable = '#'

def tilt_up(rock_map):
    sum_load = 0
    max_load_num = len(rock_map)
    last_empty_row_in_col = [1 if rock == immovable else 0 for rock in rock_map[0]]

    for row, rock_row in enumerate(rock_map):
        for col, rock in enumerate(rock_row):
            if rock == movable:
                sum_load += max_load_num - last_empty_row_in_col[col]
                last_empty_row_in_col[col] += 1
            elif rock == immovable:
                last_empty_row_in_col[col] = row + 1
    return sum_load

rock_map = read_input('input.txt')
result = tilt_up(rock_map)
print(result)
