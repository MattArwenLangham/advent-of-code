import re

def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

down = [1, 0]
right = [0, 1]
up = [-1, 0]
left = [0, -1]

pipe_map_str = read_input()

def split_lines():
    new_pipe_map = []
    for pipe_line in pipe_map_str:
        new_pipe_map.append(list(pipe_line))
    return new_pipe_map

def find_starting_point():
    for line, pipe_map_line in enumerate(pipe_map_str):
        animal_index = pipe_map_line.find('S')
        if animal_index >= 0:
            return [line, animal_index]

animal_indices = find_starting_point()
pipe_map = split_lines()

def print_map():
    for pipe_line in pipe_map:
        print(''.join(pipe_line))

def find_first_move(animal_indices, direction_to_check_dict):
    directions = [right, up, left, down]
    animal_x, animal_y = animal_indices
    for index, [x, y] in enumerate(directions):
        check_x = animal_x + x
        check_y = animal_y + y
        if check_x >= 0 and check_y >= 0:
            symbol = pipe_map[check_x][check_y]
            if symbol in direction_to_check_dict and direction_to_check_dict[symbol][index] != False:
                    return [check_x, check_y], direction_to_check_dict[symbol][index]

def get_next_move(animal_indices, direction_to_check_dict, next_move_index):
    directions = [right, up, left, down]
    x, y = directions[next_move_index]
    animal_x, animal_y = animal_indices
    new_animal_indices = [animal_x + x, animal_y + y]
    next_symbol = pipe_map[animal_x + x][animal_y + y]
    return new_animal_indices, direction_to_check_dict[next_symbol][next_move_index]

def transform_ground(animal_indices, row_direction, column_direction):
    #x is the row
    #y is the value
    curr_row, curr_column = animal_indices
    if row_direction and curr_column:
        curr_column += row_direction
        while curr_column >= 0 and curr_column < len(pipe_map[0]):
            if pipe_map[curr_row][curr_column] == '.' or pipe_map[curr_row][curr_column] == '1':
                pipe_map[curr_row][curr_column] = '1'
                curr_column += row_direction
            else:
                curr_column = -1
        curr_column = animal_indices[1]
    
    if column_direction and curr_row:
        curr_row += column_direction
        while curr_row >= 0 and curr_row < len(pipe_map):
            if pipe_map[curr_row][curr_column] == '.' or pipe_map[curr_row][curr_column] == '1':
                pipe_map[curr_row][curr_column] = '1'
                curr_row += column_direction
            else:
                curr_row = -1
        curr_row = animal_indices[0]

    if column_direction and row_direction:
        curr_row += column_direction
        curr_column += row_direction
        while curr_row >= 0 and curr_row < len(pipe_map) and curr_column >= 0 and curr_column < len(pipe_map[0]):
            if pipe_map[curr_row][curr_column] == '.' or pipe_map[curr_row][curr_column] == '1':
                pipe_map[curr_row][curr_column] = '1'
                curr_row += column_direction
                curr_column += row_direction
            else:
                curr_row = -1
    return

def change_ground_around_animal_indices(animal_indices, next_move_index, last_move_index):
    directions_index = ['right', 'up', 'left', 'down']
    directions = directions_index[last_move_index] + ' ' + directions_index[next_move_index]
    #print(pipe_map[animal_indices[0]][animal_indices[1]], directions)
    #row, column
    #print(pipe_map[animal_indices[0]][animal_indices[1]], directions)
    if directions == "left left": transform_ground(animal_indices, False, 1)
    elif directions == "left up": transform_ground(animal_indices, -1, 1),
    elif directions == "left down": transform_ground(animal_indices, 1, 1)
    elif directions == "right right": transform_ground(animal_indices, False, -1),
    elif directions == "right up": transform_ground(animal_indices, -1, -1),
    elif directions == "right down": transform_ground(animal_indices, -1, -1) #[0] unsure
    elif directions == "down right": transform_ground(animal_indices, 1, -1), #[0] unsure
    elif directions == "up up": transform_ground(animal_indices, -1, False),
    elif directions ==  "up right": transform_ground(animal_indices, -1, -1), #[0] unsure
    elif directions == "up left": transform_ground(animal_indices, -1, 1)
    elif directions == "down down": transform_ground(animal_indices, 1, False),
    elif directions == "down left": transform_ground(animal_indices, 0, -1),

def count_inside_space():
    total_count = 0
    for line in pipe_map:
        total_count += line.count('1')
    return total_count

def detect_ground_around_loop(animal_indices):
    #gets_next_move_from_last_position [right, up, left, down]
    direction_to_check_dict = {
        '|': [False, 1, False, 3],
        '-': [0, False, 2, False],
        'L': [False, False, 1, 0],
        'J': [1, False, False, 2],
        '7': [3, 2, False, False],
        'F': [False, 0, 3, False],
        'S': [0, 0, 0, 0]
    }
    print(pipe_map[animal_indices[0]][animal_indices[1]])
    transform_ground(animal_indices, 1, 1)
    animal_indices, next_move_index = find_first_move(animal_indices, direction_to_check_dict)
    print(pipe_map[animal_indices[0]][animal_indices[1]])
    transform_ground(animal_indices, 1, 1)
    current_x, current_y = animal_indices
    last_move_index = next_move_index
    while pipe_map[current_x][current_y] != 'S':
        animal_indices, next_move_index = get_next_move(animal_indices, direction_to_check_dict, next_move_index)
        change_ground_around_animal_indices(animal_indices, next_move_index, last_move_index)
        last_move_index = next_move_index
        current_x, current_y = animal_indices
        pipe_map[current_x][current_y]
    print_map()

    return count_inside_space()

def trace_path(start):
    direction_to_check_dict = {
        '|': [False, 1, False, 3],
        '-': [0, False, 2, False],
        'L': [False, False, 1, 0],
        'J': [1, False, False, 2],
        '7': [3, 2, False, False],
        'F': [False, 0, 3, False],
        'S': [0, 0, 0, 0]
    }
    coordinates = [start]
    animal_indices, next_move_index = find_first_move(start, direction_to_check_dict)
    coordinates.append(animal_indices)
    while pipe_map[animal_indices[0]][animal_indices[1]] != 'S':
        animal_indices, next_move_index = get_next_move(animal_indices, direction_to_check_dict, next_move_index)
        coordinates.append(animal_indices)
    return coordinates

def replace_unused_pipes_with_dot(coordinates):
    for x, line in enumerate(pipe_map):
        for y, value in enumerate(line):
            if re.match(r"[-LJ7FS\|]", value) and [x, y] not in coordinates:
                pipe_map[x][y] = '.'

coordinates = trace_path(animal_indices)
replace_unused_pipes_with_dot(coordinates)
print_map()
print()
result = detect_ground_around_loop(animal_indices)
print(result)