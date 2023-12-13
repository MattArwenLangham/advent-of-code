def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().split("\n\n")

def verify_reflection(pattern, i):
    print("VERIFYING", i , "in", len(pattern))
    mod = -3
    for j in range(i, len(pattern)):
        if j + mod >= 0:
            print("comparing", j, "and", j + mod, pattern[j], pattern[j + mod])
            if pattern[j] != pattern[j + mod]:
                return False
        else:
            return True
        mod -= 2
    return True

def find_horizontal_mirror_line(pattern):
    pattern_rows = pattern.split("\n")
    for i, row in enumerate(pattern_rows):
        if i == len(pattern_rows) - 1:
            return 0
        elif row == pattern_rows[i + 1]:
            print("MATCH FOUND", row, pattern_rows[i + 1], "at", i)
            if i == 0 or i == len(pattern) - 2 or verify_reflection(pattern_rows, i + 2):
                return (i + 1) * 100

def find_vertical_mirror_line(pattern):
    pattern_cols = list(map(list, zip(*pattern.split("\n"))))
    for i, col in enumerate(pattern_cols):
        if i == len(pattern_cols) - 1:
            return 0
        elif col == pattern_cols[i + 1]:
            print("MATCH FOUND", col, pattern_cols[i + 1], "at", i)
            if i == 0 or verify_reflection(pattern_cols, i + 2):
                return i + 1

def calculate_sum_of_mirrors_in_pattern_map(pattern_map):
    sum = 0
    for pattern in pattern_map:
        print("---------------")
        to_add = 0
        to_add += find_horizontal_mirror_line(pattern)
        if to_add:
            print("FOUND adding", to_add)
        if not to_add:
            to_add += find_vertical_mirror_line(pattern)
            print("FOUND adding", to_add)
        sum += to_add
    return sum

pattern_map = read_input("input.txt")
result = calculate_sum_of_mirrors_in_pattern_map(pattern_map)
print(result)