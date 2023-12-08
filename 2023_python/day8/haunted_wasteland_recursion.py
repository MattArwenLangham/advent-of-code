import re

def read_input():
    f = open("test_input.txt", "r")
    fr = re.sub(r'\s=|\(|\)|,', '', f.read())
    return fr.split("\n")

def map_documents_to_map_dict(map_documents):
    map_dict = {}
    directions = map_documents.pop(0)
    print(directions)
    for document in map_documents:
        print(document)
        key, left, right = document.split(" ")
        map_dict[key] = [left, right]
    return directions, map_dict

def get_next_key(direction_pos, directions, key, map_dict):
    direction = directions[direction_pos]
    next_direction_pos = direction_pos + 1
    total_steps = 1
    
    if key == 'ZZZ':
        return 0
    
    if next_direction_pos == len(directions):
        next_direction_pos = 0

    left, right = map_dict[key]
    if direction is 'L':
        return total_steps + get_next_key(next_direction_pos, directions, left, map_dict)
    else:
        return total_steps + get_next_key(next_direction_pos, directions, right, map_dict)

def find_steps_in_map_dict(map_dict, directions):
    starting_key = "AAA"
    total_steps = get_next_key(0, directions, starting_key, map_dict)
    return total_steps

map_documents = read_input()
directions, map_dict = map_documents_to_map_dict(map_documents)
steps_taken = find_steps_in_map_dict(map_dict, directions)
print(steps_taken)