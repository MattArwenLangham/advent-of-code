import re

def read_input():
    f = open("input.txt", "r")
    return f.read().replace(":", "").split("\n")

def raw_almanac_to_almanac_dict(raw_almanac):
    almanac_dict = {}
    
    current_almanac_key = ""

    for line in raw_almanac:
        if line:
            if len(almanac_dict) == 0:
                almanac_key, *almanac_values = line.split(" ")
                almanac_int_vaues = [int(x) for x in almanac_values]
                almanac_dict[almanac_key] = almanac_int_vaues
            elif line[0].isalpha():
                almanac_key = line[:-4]
                current_almanac_key = almanac_key
                almanac_dict[current_almanac_key] = []
            else:
                almanac_string_list = line.split(" ")
                almanac_int_list = [int(x) for x in almanac_string_list]
                almanac_dict[current_almanac_key].append(almanac_int_list)
    return almanac_dict

def find_next_number(numbers_to_check, current_number):
    for number_to_return, number_to_check, range in numbers_to_check:
        if current_number >= number_to_check and current_number < number_to_check + range:
            difference = number_to_return - number_to_check
            return current_number + difference
    return current_number


def find_lowest_location_for_seed(almanac_dict):
    seeds_to_check_list = almanac_dict["seeds"]
    process_list = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    seed_location_list = []
    for seed in seeds_to_check_list:
        current_number = seed
        for process in process_list:
            numbers_to_check = almanac_dict[process]
            current_number = find_next_number(numbers_to_check, current_number)
        seed_location_list.append(current_number)
    
    return min(seed_location_list)



raw_almanac = read_input()
almanac_dict = raw_almanac_to_almanac_dict(raw_almanac)
print(find_lowest_location_for_seed(almanac_dict))