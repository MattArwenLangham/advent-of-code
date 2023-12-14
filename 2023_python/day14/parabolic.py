def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

movable = 'O'
immovable = '#'

def tilt_up(rock_map):
    sum_load = 0
    max_load_num = len(rock_map)
    last_empty_space = [1 if rock == immovable else 0 for rock in rock_map[0]]

    for line, rock_line in enumerate(rock_map):
        for i, rock in enumerate(rock_line):
            if rock == movable:
                sum_load += max_load_num - last_empty_space[i]
                last_empty_space[i] += 1
            elif rock == immovable:
                last_empty_space[i] = line + 1

    return sum_load

rock_map = read_input()
result = tilt_up(rock_map)
print(result)
