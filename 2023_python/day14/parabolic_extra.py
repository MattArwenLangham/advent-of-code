movable = 'O'
immovable = '#'

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().split("\n")

def rock_map_to_md_list(rock_map_raw):
    rock_map = []
    for rock_line in rock_map_raw:
        rock_map.append(list(rock_line))
    return rock_map

def print_rock_map(rock_map):
    print()
    for rock_line in rock_map:
        print(''.join(rock_line))
    print()

def tilt(rock_map):
    last_empty_space = [1 if rock == immovable else 0 for rock in rock_map[0]]
    for line, rock_line in enumerate(rock_map):
        for i, rock in enumerate(rock_line):
            if rock == movable:
                rock_line[i] = '.'
                rock_map[last_empty_space[i]][i] = 'O'
                last_empty_space[i] += 1
            elif rock == immovable:
                last_empty_space[i] = line + 1
    return rock_map

def turn_left(rock_map):
    rotated_rock_map = [list(row)[::-1] for row in zip(*rock_map)]
    return rotated_rock_map

def sum_rock_map(rock_map):
    load_sum = 0
    max_load = len(rock_map)
    for i, rock_line in enumerate(rock_map):
        load_sum += rock_line.count(movable) * (max_load - i)
    return load_sum

def spin_cycle(rock_map, times):
    i = 1
    while i < times - 1:
        #North
        tilt(rock_map)
        #East
        rock_map = turn_left(rock_map)
        rock_map = tilt(rock_map)
        #South
        rock_map = turn_left(rock_map)
        rock_map = tilt(rock_map)
        #West
        rock_map = turn_left(rock_map)
        rock_map = tilt(rock_map)

        rock_map = turn_left(rock_map)
        load_sum = sum_rock_map(rock_map)
        i += 1
        print(load_sum)

rock_map_raw = read_input('input.txt')
rock_map = rock_map_to_md_list(rock_map_raw)
spin_cycle(rock_map, 400)

#Answer should be 99291