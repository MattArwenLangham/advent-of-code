import re
import string

def read_input():
    f = open("test_input.txt", "r")
    return f.read().replace(":", "").strip().split("\n")

def pair_boat_result_times_and_distance(raw_boat_results):
    times = raw_boat_results[0].split()[1:]
    distances = raw_boat_results[1].split()[1:]
    return list(zip(times, distances))

def find_boat_result_possibilities(boat_result):
    possible_times = 0
    time, distance_to_find = boat_result
    button_hold = 0
    test_time = 0
    for button_hold in range(int(time)):
        test_time -= button_hold
        speed = button_hold
        distance_travelled = speed * (int(time) - button_hold)
        if distance_travelled > int(distance_to_find):
            possible_times += 1
    return possible_times

def find_margin_of_error_in_boat_results(boat_results):
    margin_of_error = 1
    for boat_result in boat_results:
        margin_of_error *= find_boat_result_possibilities(boat_result)
    return margin_of_error

raw_boat_results = read_input()
boat_results = pair_boat_result_times_and_distance(raw_boat_results)
margin_of_error = find_margin_of_error_in_boat_results(boat_results)
print(margin_of_error)