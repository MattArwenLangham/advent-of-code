planet = '#'
distance_modification = 2

def read_input():
    f3d_list = []
    f = open("input.txt", "r")
    f_lines = f.read().split("\n")
    for f_line in f_lines:
        f3d_list.append(list(f_line))
    return f3d_list

def print_map(map):
    for map_line in map:
        print(''.join(map_line))

def get_indexes_to_modify(galaxy_map):
    rows_to_modify = []
    columns_to_modify = []
    for index, galaxy_row in enumerate(galaxy_map):
        if not planet in galaxy_row:
            rows_to_modify.append(index)
        if not planet in [column[index] for column in galaxy_map]:
            columns_to_modify.append(index)
    return [rows_to_modify, columns_to_modify]

def get_indexes_of_planets(galaxy_map):
    planet_indexes = []
    for x, galaxy_line in enumerate(galaxy_map):
        if planet in galaxy_line:
            for y, galaxy_space in enumerate(galaxy_line):
                if galaxy_space == planet:
                    planet_indexes.append([x, y])
    return planet_indexes

def find_modified_lines_crossed(a, b, modified_lines):
    if a <= b:
        return list(filter(lambda x: a < x < b, modified_lines))
    else:
        return list(filter(lambda x: b < x < a, modified_lines))


def add_distances_from_other_planets(planet_indexes, indexes_to_modify):
    distances_sum = 0
    rows_to_modify, columns_to_modify = indexes_to_modify
    for index, planet_index in enumerate(planet_indexes):
        for x in range(index + 1, len(planet_indexes)):
            a, b = planet_index
            c, d = planet_indexes[x]
            modified_rows_crossed = find_modified_lines_crossed(a, c, rows_to_modify)
            modified_columns_crossed = find_modified_lines_crossed(b, d, columns_to_modify)
            total_crossed = len(modified_rows_crossed) + len(modified_columns_crossed)
            e = (total_crossed * distance_modification) - total_crossed
            distance = abs(a - c) + abs(b - d) + e
            distances_sum += distance

    return distances_sum

galaxy_map = read_input()
indexes_to_modify = get_indexes_to_modify(galaxy_map)
planet_indexes = get_indexes_of_planets(galaxy_map)
result = add_distances_from_other_planets(planet_indexes, indexes_to_modify)
print(result)