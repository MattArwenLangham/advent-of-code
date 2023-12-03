import re

def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

schematic_lines = read_input()

def map_gears_to_indexes(schematic_lines):
    gear_indexes = []
    for schematic_line in schematic_lines:
        matches = [match.start() for match in re.finditer(r'\*', schematic_line)]
        gear_indexes.append(matches)
    return gear_indexes

def get_number_from_index(line, position):
    numbers_in_line = re.finditer(r'\d+', schematic_lines[line])
    for number in numbers_in_line:
        if number.span()[0] <= position and number.span()[1] >= position:
            return int(number.group(0))

def get_numbers_adjacent(line, position):
    numbers_adjacent = []
    modifiers = [-1, 0, 1]
    for line_modifier in modifiers:
        for position_modifier in modifiers:
            gear_to_check = schematic_lines[line + line_modifier][position + position_modifier]
            try:
                int(gear_to_check)
                number = get_number_from_index(line + line_modifier, position + position_modifier)
                if number not in numbers_adjacent:
                    numbers_adjacent.append(number)
            except:
                pass
            
    if len(numbers_adjacent) == 2:
        return numbers_adjacent[0] * numbers_adjacent[1]

def get_gear_ratio_sum_from_gear_indexes_list(gear_indexes_list):
    gear_ratio_sum = 0
    for line, positions in enumerate(gear_indexes_list):
        if positions:
            for position in positions:
                gear_ratio = get_numbers_adjacent(line, position)
                if gear_ratio:
                    gear_ratio_sum += gear_ratio
    return gear_ratio_sum

gear_indexes_list = map_gears_to_indexes(schematic_lines)
gear_ratio_sum = get_gear_ratio_sum_from_gear_indexes_list(gear_indexes_list)
print(gear_ratio_sum)