import re

def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

schematic_lines = read_input()

def map_symbols_to_indexes(schematic_lines):
    symbol_indexes = []
    for schematic_line in schematic_lines:
        matches = [match.start() for match in re.finditer(r'[^\w\s.]', schematic_line)]
        symbol_indexes.append(matches)
    return symbol_indexes

def get_number_from_index(line, position):
    numbers_in_line = re.finditer(r'\d+', schematic_lines[line])
    for number in numbers_in_line:
        if number.span()[0] <= position and number.span()[1] >= position:
            return number.group(0)

def get_numbers_adjacent(line, position):
    numbers_adjacent = []
    modifiers = [-1, 0, 1]
    for line_modifier in modifiers:
        for position_modifier in modifiers:
            symbol_to_check = schematic_lines[line + line_modifier][position + position_modifier]
            try:
                int(symbol_to_check)
                number = get_number_from_index(line + line_modifier, position + position_modifier)
                if number not in numbers_adjacent:
                    numbers_adjacent.append(number)
            except:
                pass
    
    return numbers_adjacent

def get_part_numbers_from_symbol_indexes_list(symbol_indexes_list):
    part_numbers = []
    for line, positions in enumerate(symbol_indexes_list):
        if positions:
            for position in positions:
                numbers_adjacent = get_numbers_adjacent(line, position)
                part_numbers.extend(int(number) for number in numbers_adjacent if number not in part_numbers)
    return part_numbers

symbol_indexes_list = map_symbols_to_indexes(schematic_lines)
part_numbers = get_part_numbers_from_symbol_indexes_list(symbol_indexes_list)
print(sum(part_numbers))