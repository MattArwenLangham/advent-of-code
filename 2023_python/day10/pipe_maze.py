def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

down = [1, 0]
right = [0, 1]
up = [-1, 0]
left = [0, -1]

def find_indices_of_animal(pipe_map):
    for line, pipe_map_line in enumerate(pipe_map):
        animal_index = pipe_map_line.find('S')
        if animal_index >= 0:
            return [line, animal_index]

def find_start_move(pipe_map, animal_indices, direction_to_check_dict):
    directions = [down, right, up, left]
    animal_x, animal_y = animal_indices
    for index, [x, y] in enumerate(directions):
        check_x = animal_x + x
        check_y = animal_y + y
        if check_x >= 0 and check_y >= 0:
            symbol = pipe_map[check_x][check_y]
            if symbol in direction_to_check_dict and direction_to_check_dict[symbol][index] != False:
                    return [check_x, check_y], direction_to_check_dict[symbol][index]

def get_next_move(pipe_map, animal_indices, direction_to_check_dict, next_move_index):
    directions = [down, right, up, left]
    x, y = directions[next_move_index]
    animal_x, animal_y = animal_indices
    new_animal_indices = [animal_x + x, animal_y + y]
    next_symbol = pipe_map[animal_x + x][animal_y + y]
    return new_animal_indices, direction_to_check_dict[next_symbol][next_move_index]
    
def find_num_of_steps_in_pipe_loop(pipe_map, animal_indices):
    #gets_next_move_from_last_position [down, right, up, left]
    direction_to_check_dict = {
        '|': [0, False, 2, False],
        '-': [False, 1, False, 3],
        'L': [1, False, False, 2],
        'J': [3, 2, False, False],
        '7': [False, 0, 3, False],
        'F': [False, False, 1, 0],
        'S': [0, 0, 0, 0]
    }

    animal_indices, next_move_index = find_start_move(pipe_map, animal_indices, direction_to_check_dict)
    times_moved = 1
    current_x, current_y = animal_indices
    while pipe_map[current_x][current_y] != 'S':
        animal_indices, next_move_index = get_next_move(pipe_map, animal_indices, direction_to_check_dict, next_move_index)
        current_x, current_y = animal_indices
        times_moved += 1

    return int(times_moved / 2)

def find_furthest_point_in_pipe_loop(pipe_map, animal_indices):
    num_of_steps = find_num_of_steps_in_pipe_loop(pipe_map, animal_indices)
    return num_of_steps

pipe_map = read_input()
animal_indices = find_indices_of_animal(pipe_map)
print(animal_indices)
result = find_furthest_point_in_pipe_loop(pipe_map, animal_indices)
print(result)