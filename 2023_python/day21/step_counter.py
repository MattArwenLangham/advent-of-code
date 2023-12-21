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

def step(garden_map, positions):
    step_directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    next_steps = []
    for position in positions:
        for step_direction in step_directions:
            x, y = position
            i, j = step_direction
            if x + i < 0 or x + i > len(garden_map):
                break
            if y + j < 0 or y + j > len(garden_map[0]):
                break
            if garden_map[x + i][y + j] == '.':
                garden_map[x + i][y + j] = 'O'
                next_steps.append([x + i, y + j])
            garden_map[x][y] = '.'
    return next_steps

def find_max_num_of_steps(step_num, garden_map, start_position):
    steps_from = [[start_position]]
    for i in range(0, step_num):
        new_steps = []
        for step_from in steps_from:
            new_steps.append(step(garden_map, step_from))
        steps_from = list(new_steps)
    return garden_map

def sum_possible_steps(garden_map):
    sum = 0
    for line in garden_map:
        sum += line.count("O")
    return sum

garden_map = read_input('input.txt')
start_position = find_starting_position(garden_map)
final_garden_map = find_max_num_of_steps(64, garden_map, start_position)
result = sum_possible_steps(final_garden_map)
print(result)