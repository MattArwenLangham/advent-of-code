from itertools import combinations
import re

def read_input():
    f = open("test_input.txt", "r")
    return f.read().split("\n")

def split_to_subsections(hot_springs_line_map):
    return re.sub('\.\.+', '.', hot_springs_line_map).strip('.').split(".")

def calculate_possibilities(values, total_value, subsection):
    print("Calculating possibility", values)
    opts = combinations(range(len(values) + len(subsection) - total_value), len(values))
    amount_of_opts= 0
    for opt in opts:
        amount_of_opts += 1
    return amount_of_opts

def find_exhausted_values(spaces_left, broken_list):
    exhausted_values = []
    broken_sum = sum(broken_list) + (len(broken_list) - 1)
    while broken_sum > spaces_left:
        exhausted_value = broken_list.pop(0)
        exhausted_values.append(exhausted_value)
        broken_sum -= exhausted_value + 1
    print("Exhausted Values in func", exhausted_values)
    return exhausted_values

def get_valid_possibilities(hot_spring_subsections, broken_list):
    print(hot_spring_subsections)
    spaces_left  = len(''.join(hot_spring_subsections))
    all_possibilities = []
    exhausted_values = []
    for index, subsection in enumerate(hot_spring_subsections):
        print("subsection", subsection)
        total_value = 0
        values = []
        possibilities = []
        broken_list_looped = False
        current_indexes = []
        while total_value <= len(subsection) and not broken_list_looped:
            print(total_value, len(subsection))
            print("EXHAUSTED VALUES", exhausted_values)
            for exhausted_value in exhausted_values:
                possibilities.append(None)
            
            for index, value in enumerate(broken_list):
                
                print("Broken_list", broken_list)
                total_value += value
                values.append(value)
                print("Total value", total_value, "Subsection length", len(subsection), "Value" , value, "Broken List", broken_list)
                if total_value <= len(subsection):
                    possibilities.append(calculate_possibilities(values, total_value, subsection))
                    print(possibilities, "Possibilities calculated in total")
                    total_value += 1
            broken_list_looped = True
        all_possibilities.append(possibilities)
        print("Too big")
        spaces_left -= len(subsection)
        exhausted_values.extend(find_exhausted_values(spaces_left, broken_list))
        broken_list_looped = False
    print(all_possibilities)
    #return sum(all_possibilities)

def get_sum_of_valid_possibilities(hot_springs_fieldmap):
        valid_possibilities = 0
        for hot_springs_line in hot_springs_fieldmap:
            hot_springs_line_map, broken_list = hot_springs_line.split(" ")
            broken_list = [int(x) for x in broken_list.split(",")]
            
            hot_spring_subsections = split_to_subsections(hot_springs_line_map)
            valid_possibilities = get_valid_possibilities(hot_spring_subsections, broken_list)

        return valid_possibilities

hot_springs_fieldmap = read_input()
result = get_sum_of_valid_possibilities(hot_springs_fieldmap)
print(result)