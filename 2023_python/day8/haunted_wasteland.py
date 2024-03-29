import re

def read_input():
    f = open("input.txt", "r")
    fr = re.sub(r'\s=|\(|\)|,', '', f.read())
    return fr.split("\n")

def map_documents_to_map_dict(map_documents):
    map_dict = {}
    directions = map_documents.pop(0)
    for document in map_documents:
        key, left, right = document.split(" ")
        map_dict[key] = [left, right]
    return directions, map_dict

def find_steps_in_map_dict(map_dict, directions):
    total_steps = 0
    current_direction_pos = 0
    current_key = "AAA"
    
    while not current_key == "ZZZ":
        if current_direction_pos == len(directions):
            current_direction_pos = 0

        direction = directions[current_direction_pos]
        left, right = map_dict[current_key]

        current_key = left if direction == 'L' else right
        
        total_steps += 1
        current_direction_pos += 1

    return total_steps

map_documents = read_input()
directions, map_dict = map_documents_to_map_dict(map_documents)
steps_taken = find_steps_in_map_dict(map_dict, directions)
print(steps_taken)