def read_input(file_path):
    with open(file_path, 'r') as file:
        processed_map = []
        lines = file.read().split("\n")
        for line in lines:
            processed_map.append(list(line))
        return processed_map

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

object_dict = {
    'right_mirror': '/',
    'left_mirror': '\\',
    'vertical_splitter': '|',
    'horizontal_splitter': '-',
    'horizontal_splitter_used': '=',
    'vertical_splitter_used': ':'
}

def print_floor_map(floor_map):
    for line in floor_map:
        print(''.join(line))

def get_next_index(current_index, direction):
    current_index[0] += direction[0]
    current_index[1] += direction[1]
    return current_index

def is_current_tile_in_range(floor_map, current_index):
    max_row = len(floor_map)
    max_col = len(floor_map[0])
    row, col = current_index
    if row < 0 or row >= max_row or col < 0 or col >= max_col:
        return False
    else:
        return True

def has_object_been_passed(object_list, tile_to_check):
    for tile in object_list:
        if tile[0] == tile_to_check[0] and tile[1] == tile_to_check[1]:
           return True 
    return False

def find_all_energised_tiles(floor_map, current_index, direction, tiles_energised):
    tiles_to_energise = tiles_energised
    beam_moving = True
    if is_current_tile_in_range(floor_map, current_index):
        current_index = current_index
        last_index = [0, 0]
        while beam_moving:
            current_tile = floor_map[current_index[0]][current_index[1]]

            if current_tile == '.':
                floor_map[current_index[0]][current_index[1]] = '#'
            
            if not current_tile == '.' and not current_tile == '#' and not has_object_been_passed(tiles_to_energise, current_index):
                tiles_to_energise.append([current_index[0], current_index[1]])
            
            if current_tile == object_dict['left_mirror']:
                if direction == right: direction = down
                elif direction == left: direction = up
                elif direction == down: direction = right
                else: direction = left
            elif current_tile == object_dict['right_mirror']:
                if direction == right: direction = up
                elif direction == left: direction = down
                elif direction == down: direction = left
                else: direction = right
            elif current_tile == object_dict['vertical_splitter']:
                floor_map[current_index[0]][current_index[1]] = object_dict['vertical_splitter_used']

                if direction == left or direction == right:
                    last_index[0], last_index[1] = current_index
                    next_index = get_next_index(current_index, up)
                    if is_current_tile_in_range(floor_map, next_index):
                        floor_map, tiles_to_energise = find_all_energised_tiles(floor_map, next_index, up, tiles_energised)
                        current_index[0], current_index[1] = last_index
                    direction = down

            elif current_tile == object_dict['vertical_splitter_used']:
                if direction == left or direction == right:
                    return floor_map, tiles_to_energise
                
            elif current_tile == object_dict['horizontal_splitter']:
                
                floor_map[current_index[0]][current_index[1]] = object_dict['horizontal_splitter_used']

                if direction == down or direction == up:
                    last_index[0], last_index[1] = current_index
                    next_index = get_next_index(current_index, left)
                    if is_current_tile_in_range(floor_map, next_index):
                        floor_map, tiles_to_energise = find_all_energised_tiles(floor_map, next_index, left, tiles_energised)
                    current_index[0], current_index[1] = last_index
                    direction = right

            elif current_tile == object_dict['horizontal_splitter_used']:
                if direction == down or direction == up:                    
                    return floor_map, tiles_to_energise

            current_index = get_next_index(current_index, direction)
            if not is_current_tile_in_range(floor_map, current_index):
                return floor_map, tiles_to_energise

    return floor_map, tiles_to_energise

def sum_all_energised(floor_map, tiles_to_energise):
    sum_of_energised_tiles = len(tiles_to_energise)
    for line in floor_map:
        sum_of_energised_tiles += line.count('#')
    return sum_of_energised_tiles

floor_map = read_input('input.txt')
max_sum = 0
file = 'input.txt'
#run down
for i in range(0, len(floor_map[0])):
    floor_map = read_input(file)
    floor_map, tiles_to_energise = find_all_energised_tiles(floor_map, [0, i], down, [])
    sum = sum_all_energised(floor_map, tiles_to_energise)
    if sum > max_sum: max_sum = sum

#run right
for i in range(0, len(floor_map)):
    floor_map = read_input(file)
    floor_map, tiles_to_energise = find_all_energised_tiles(floor_map, [i, 0], right, [])
    sum = sum_all_energised(floor_map, tiles_to_energise)
    if sum > max_sum: max_sum = sum

#run left
for i in range(0, len(floor_map)):
    floor_map = read_input(file)
    floor_map, tiles_to_energise = find_all_energised_tiles(floor_map, [i, len(floor_map[0]) - 1], left, [])
    sum = sum_all_energised(floor_map, tiles_to_energise)
    if sum > max_sum: max_sum = sum

#run up
for i in range(0, len(floor_map[0])):
    floor_map = read_input(file)
    floor_map, tiles_to_energise = find_all_energised_tiles(floor_map, [len(floor_map) - 1, i], up, [])
    sum = sum_all_energised(floor_map, tiles_to_energise)
    if sum > max_sum: max_sum = sum

print(max_sum)