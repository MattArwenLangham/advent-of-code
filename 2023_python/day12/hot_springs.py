from itertools import combinations

def read_input():
    f = open("test_input.txt", "r")
    return f.read().split("\n")

def get_all_possibilities(empty_spaces, num_of_groups, sizes):
    opts = combinations(range(num_of_groups + empty_spaces), num_of_groups)
    possibility_list = []
    for opt in opts:
        possibility = []
        start = 0
        for i, pos in enumerate(opt):
            start += pos
            if i > 0:
               start -= opt[i - 1]
            size = sizes[i]
            possibility.extend(range(start, start + size))
            start += size
        possibility_list.append(possibility)
    return possibility_list

def get_num_of_valid_possibilities(possibility_list, hot_springs_line_map):
    definite_working_spaces = [i for i, ltr in enumerate(hot_springs_line_map) if ltr == '.']
    definite_broken_spaces = [i for i, ltr in enumerate(hot_springs_line_map) if ltr == '#']
    possibilities_without_working_spaces = [possibility for possibility in possibility_list if not any(i in possibility for i in definite_working_spaces)]
    valid_possibilities = [possibility for possibility in possibilities_without_working_spaces if all(i in possibility for i in definite_broken_spaces)]
    return(len(valid_possibilities))


def get_sum_of_valid_possibilities(hot_springs_fieldmap):
    valid_possibilities = 0

    for hot_springs_line in hot_springs_fieldmap:
        hot_springs_line_map, hot_springs_line_broken_list = hot_springs_line.split(" ")
        contigious_broken_list = [int(x) for x in hot_springs_line_broken_list.split(",")]

        spaces_available = len(hot_springs_line_map)
        groups_of_broken = len(contigious_broken_list)
        sum_of_broken = sum(contigious_broken_list)
        spaces_needed_between = groups_of_broken - 1
        spaces_empty = spaces_available - (sum_of_broken + spaces_needed_between)
        hot_springs_line_map.count("#")

        possibility_list = get_all_possibilities(spaces_empty, groups_of_broken, contigious_broken_list)
        print(len(possibility_list))
        valid_possibilities += get_num_of_valid_possibilities(possibility_list, hot_springs_line_map)

    return valid_possibilities

hot_springs_fieldmap = read_input()
result = get_sum_of_valid_possibilities(hot_springs_fieldmap)
