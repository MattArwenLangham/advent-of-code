def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

def predict_next_lines_of_data(first_line_of_data):
    first_line_of_int = [eval(i) for i in first_line_of_data]
    lines_of_data = [first_line_of_int]
    line_of_data = first_line_of_int

    while any(line_of_data):
        new_line_of_data = []
        for index, value in enumerate(line_of_data):
            if index > 0:
                new_line_of_data.append(value - line_of_data[index - 1])
        lines_of_data[:0] = [new_line_of_data]
        line_of_data = new_line_of_data
    return lines_of_data

def get_past_history_of_data(data):
    for index, line in enumerate(data):
        if index:
            extrapolated_data = line[0] - data[index - 1][0]
            line.insert(0, extrapolated_data)
    return data

def get_value_of_extrapolated_past_data(past_data):
    return past_data[-1][0]

def sum_extrapolated_oasis_data(oasis_data):
    sum_of_extrapolated_past_data = 0
    for first_line_of_data in oasis_data:
        future_data = predict_next_lines_of_data(first_line_of_data.split(" "))
        past_and_future_data = get_past_history_of_data(future_data)
        sum_of_extrapolated_past_data += get_value_of_extrapolated_past_data(past_and_future_data)
    return sum_of_extrapolated_past_data

oasis_data = read_input()
result = sum_extrapolated_oasis_data(oasis_data)
print(result)