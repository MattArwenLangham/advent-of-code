def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

def predict_next_lines_of_data(first_line_of_data):
    first_line_of_int = [eval(i) for i in first_line_of_data]
    lines_of_data = [first_line_of_int]
    line_of_data = first_line_of_int

    while not all(value == 0 for value in line_of_data):
        new_line_of_data = []
        for index, value in enumerate(line_of_data):
            if index > 0:
                new_line_of_data.append(value - line_of_data[index - 1])
        lines_of_data[:0] = [new_line_of_data]
        line_of_data = new_line_of_data
    return lines_of_data
    
def get_value_of_extrapolated_future_data(future_data):
    extrapolated_data_sum = 0
    for line in future_data:
        extrapolated_data_sum += line[-1]
    return extrapolated_data_sum

def sum_extrapolated_oasis_data(oasis_data):
    sum_of_extrapolated_future_data = 0
    for first_line_of_data in oasis_data:
        future_data = predict_next_lines_of_data(first_line_of_data.split(" "))
        sum_of_extrapolated_future_data += get_value_of_extrapolated_future_data(future_data)
    return sum_of_extrapolated_future_data

oasis_data = read_input()
result = sum_extrapolated_oasis_data(oasis_data)
print(result)