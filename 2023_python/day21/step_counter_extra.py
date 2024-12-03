import math

def read_input(file_path):
    with open(file_path, 'r') as file:
        garden_map_list = []
        lines = file.read().split("\n")
        for line in lines:
            garden_map_list.append(list(line))
        return garden_map_list

def print_map(map):
    for line in map:
        print(''.join(line))

def find_starting_position(garden_map):
    for i, line in enumerate(garden_map):
        if 'S' in line:
            return [i, line.index('S')]

def no_duplicates(step_to_add, next_steps):
    if len(next_steps) == 0:
        return True
    
    for step in next_steps:
        if step[0] == step_to_add[0] and step[1] == step_to_add[1]:
            return False
    
    return True

edges_touched = []
loop_point = []

def add_edge_touched(modified_x, modified_y, garden_map):
    x_edge = len(garden_map) - 1
    y_edge = len(garden_map[0]) - 1
    if (modified_x == x_edge or modified_x == 0) or (modified_y == y_edge or modified_y == 0):
        if modified_x > x_edge or modified_x < 0 or modified_y > y_edge or modified_y < 0: return
        if no_duplicates([modified_x, modified_y], edges_touched):
            edges_touched.append([modified_x, modified_y])

def get_possible_spaces_in_grid(garden_map):
    blocked_spaces = 0
    for line in garden_map:
        blocked_spaces += line.count("#")
    return (len(garden_map) * len(garden_map[0])) - blocked_spaces

grids_account_for = [0, 0]

def step(garden_map, positions):
    step_directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    next_steps = []

    if len(edges_touched) > len(garden_map) + len(garden_map[0]):
        total_grid = get_possible_spaces_in_grid(garden_map)
        grids_account_for[1] = math.ceil(total_grid / 2)
        grids_account_for[0] = math.floor(total_grid / 2)
    for position in positions:
        for step_direction in step_directions:
            x, y = position
            i, j = step_direction
            modified_x = x + i
            modified_y = y + j
            if modified_x == 0 or modified_y == 0:
                add_edge_touched(modified_x, modified_y, garden_map)
            
            if modified_x < 0:
                while modified_x < 0:
                    modified_x += len(garden_map)
            elif modified_x >= len(garden_map) - 1:
                add_edge_touched(modified_x, modified_y, garden_map)
                while modified_x >= len(garden_map):
                    modified_x -= len(garden_map)
            if modified_y < 0:
                while modified_y < 0:
                    modified_y += len(garden_map)
            elif modified_y >= len(garden_map[0]) - 1:
                add_edge_touched(modified_x, modified_y, garden_map)
                while modified_y >= len(garden_map):
                    modified_y -= len(garden_map)
            if garden_map[modified_x][modified_y] != '#' and no_duplicates([x + i, y + j], next_steps):
                next_steps.append([x + i, y + j])
    return next_steps

def find_max_num_of_steps(step_num, garden_map, start_position):
    steps_from = [[start_position]]
    for i in range(0, step_num):
        new_steps = []
        for step_from in steps_from:
            steps_to_add = step(garden_map, step_from)
            new_steps.append(steps_to_add)
        steps_from = list(new_steps)
        
        print(i, len(steps_from[0]) + grids_account_for[i % 2])

    return len(steps_from[0]) + grids_account_for[i % 2]

garden_map = read_input('test_input.txt')
start_position = find_starting_position(garden_map)
result = find_max_num_of_steps(50, garden_map, start_position)
print(result)

#1594 is 50