import string

def read_input():
    f = open("test_input.txt", "r")
    return f.read().replace(" ", "").strip().split("\n")

def pair_boat_result_times_and_distance(raw_boat_result):
    times = raw_boat_result[0].split(":")[1:]
    distances = raw_boat_result[1].split(":")[1:]
    return list(zip(times, distances))

def find_margin_of_error_in_boat_result(boat_result):
    time, distance_to_find = boat_result
    margin_of_error = 0
    
    for button_hold in range(int(time)):
        distance_travelled = button_hold * (int(time) - button_hold)
        if distance_travelled > int(distance_to_find):
            margin_of_error += 1
    return margin_of_error

raw_boat_result = read_input()
[boat_result] = pair_boat_result_times_and_distance(raw_boat_result)
margin_of_error = find_margin_of_error_in_boat_result(boat_result)
print(margin_of_error)