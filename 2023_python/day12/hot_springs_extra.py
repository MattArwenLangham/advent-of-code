from itertools import combinations

def read_input():
    f = open("test_input.txt", "r")
    return f.read().split("\n")

def add_range(start, size, definite_working_spaces, definite_broken_spaces, definite_broken_spaces_i):
    possibility = []
    i = definite_broken_spaces_i
    for x in range(start, start + size):
        if x in definite_working_spaces:
            return [], 0
        elif x == definite_broken_spaces[i]:
            i += 1
            possibility.append(x)
        elif x > definite_broken_spaces[i]:
            return [], 0
        else: 
            possibility.append(x)
    return possibility, i

def get_all_possibilities(empty_spaces, num_of_groups, sizes, definite_working_spaces, definite_broken_spaces):
    opts = combinations(range(num_of_groups + empty_spaces), num_of_groups)
    possibility_list = []
    for opt in opts:
        possibility = []
        start = 0
        definite_broken_spaces_i = 0
        for i, pos in enumerate(opt):
            start += pos
            if i > 0:
               start -= opt[i - 1]
            size = sizes[i]
            possibility_range, definite_broken_spaces_i = add_range(start, size, definite_working_spaces, definite_broken_spaces, definite_broken_spaces_i)
            start += size
            if possibility_range:
                possibility.extend(possibility_range)
            else:
                break   
        if len(possibility) == sum(sizes):
            possibility_list.append(possibility)
    return possibility_list

def get_sum_of_valid_possibilities(hot_springs_fieldmap):

    for hot_springs_line in hot_springs_fieldmap:
        hot_springs_line = hot_springs_fieldmap[0]
        hot_springs_line_map, hot_springs_line_broken_list = hot_springs_line.split(" ")
        hot_springs_line_map = (hot_springs_line_map + '?') * 4
        hot_springs_line_broken_list = (hot_springs_line_broken_list + ',') * 4
        contigious_broken_list = [int(x) for x in hot_springs_line_broken_list[:-1].split(",")]

        definite_working_spaces = [i for i, ltr in enumerate(hot_springs_line_map) if ltr == '.']
        definite_broken_spaces = [i for i, ltr in enumerate(hot_springs_line_map) if ltr == '#']
        spaces_available = len(hot_springs_line_map)
        groups_of_broken = len(contigious_broken_list)
        sum_of_broken = sum(contigious_broken_list)
        spaces_needed_between = groups_of_broken - 1
        spaces_empty = spaces_available - (sum_of_broken + spaces_needed_between)

        possibility_list = get_all_possibilities(spaces_empty, groups_of_broken, contigious_broken_list, definite_working_spaces, definite_broken_spaces)

        return len(possibility_list)

hot_springs_fieldmap = read_input()
result = get_sum_of_valid_possibilities(hot_springs_fieldmap)
print(result)