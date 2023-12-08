import re
from math import lcm

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

def find_starting_keys(map_dict):
    return [key for key in map_dict.keys() if key.endswith("A")]


def find_lowest_steps(map_dict, directions, start_key):
    total_steps = 0
    current_direction_pos = 0
    current_key = start_key
    
    while not current_key.endswith("Z"):
        if current_direction_pos == len(directions):
            current_direction_pos = 0

        direction = directions[current_direction_pos]
        left, right = map_dict[current_key]

        current_key = left if direction == 'L' else right
        
        total_steps += 1
        current_direction_pos += 1

    return total_steps


def get_lowest_steps_for_ghosts(directions, map_dict, key_list):
    ghost_steps = []
    for key in key_list:
        ghost_steps.append(find_lowest_steps(map_dict, directions, key))
    return lcm(*ghost_steps)
    

def find_lowest_ghost_steps(map_dict, directions):
    key_list = find_starting_keys(map_dict)
    return get_lowest_steps_for_ghosts(directions, map_dict, key_list)

map_documents = read_input()
directions, map_dict = map_documents_to_map_dict(map_documents)
steps_taken = find_lowest_ghost_steps(map_dict, directions)
print(steps_taken)