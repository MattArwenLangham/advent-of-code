def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().split("\n")

direction_dict = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

def print_dig_map(dig_map):
    for line in dig_map:
        print(''.join(line))

def get_dig_map(max_height, max_width):
    dig_map = []
    for i in range(0, 700):
        dig_map_line = '.' * 700
        dig_map.append(list(dig_map_line))
    return dig_map

def get_dig_instructions_and_map(raw_instructions):
    dig_instructions = []
    max_height = 1
    max_width = 1
    start_height = 0
    current_height = 0
    start_width = 0
    current_width = 0

    for instruction in raw_instructions:
        direction, amount, hex_color = instruction.split(" ")
        amount = int(amount)
        dig_instructions.append([direction_dict[direction][0] * amount, direction_dict[direction][1] * (amount)])
        #print(direction, amount)
        if direction == 'D':
            max_height += amount
            current_height += amount
        elif direction == 'U':
            current_height -= amount
            if current_height < start_height:
                start_height = current_height
        elif direction == 'R':
            max_width += amount
            current_width += amount
        elif direction =='L':
            current_width -= amount
            if current_width < start_width:
                start_width = current_width
        #print("Current height", current_height, "Max height", max_height)
        #print("Current width", current_width, "Max width", max_width)
    
    #print("Max Height", max_height, "Max Width", max_width)
    empty_dig_map = get_dig_map(max_height, max_width)
    start_position = [start_height, start_width]
    return empty_dig_map, dig_instructions, start_position, 


def fill_dig_map(empty_dig_map, row, prev_col, col_change):
    curr_col = prev_col + col_change
    if col_change > 0:
        for i in range(row + 1, len(empty_dig_map)):
            for j in range(prev_col, curr_col):
                if empty_dig_map[i][j] == '.':
                    empty_dig_map[i][j] = '-'
                if empty_dig_map[i][j] == '#':
                    return
    else:
        for i in range(row + 1, len(empty_dig_map)):
            for j in range(curr_col, prev_col):
                if empty_dig_map[i][j] == '-':
                    empty_dig_map[i][j] = '.'
                if empty_dig_map[i][j] == '#':
                    return


def generate_edges(empty_dig_map, dig_instructions, start_position):
    location = [500, 350]
    print(location)
    for instruction in dig_instructions:
        if instruction[0] > 0 or instruction[1] > 0:
            for i in range(0, instruction[0]):
                empty_dig_map[location[0] + i][location[1]] = '#'
            for i in range(0, instruction[1]):
                empty_dig_map[location[0]][location[1] + i] = '#'
        else:
            for i in range(0, abs(instruction[0])):
                empty_dig_map[location[0] - i][location[1]] = '#'
            for i in range(0, abs(instruction[1])):
                empty_dig_map[location[0]][location[1] - i] = '#'
    
        if instruction[1] != 0:
            fill_dig_map(empty_dig_map, location[0], location[1], instruction[1])

        location[0] += instruction[0]
        location[1] += instruction[1]

    return empty_dig_map

def sum_dig_spots(dig_map):
    sum = 0
    for line in dig_map:
        sum += line.count('#') + line.count('-')
    return sum

raw_instructions = read_input('input.txt')
empty_dig_map, dig_instructions, start_position = get_dig_instructions_and_map(raw_instructions)
dig_map = generate_edges(empty_dig_map, dig_instructions, start_position)
print_dig_map(dig_map)
result = sum_dig_spots(dig_map)
print(result)

#32547 - too low