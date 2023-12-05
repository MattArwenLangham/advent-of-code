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
                almanac_int_values = [int(x) for x in almanac_values]

                almanac_int_values_paired = [
                    (almanac_int_values[i], almanac_int_values[i + 1]) 
                    for i in range(0, len(almanac_int_values) - 1, 2)
                ]

                almanac_dict[almanac_key] = almanac_int_values_paired
            elif line[0].isalpha():
                almanac_key = line[:-4]
                current_almanac_key = almanac_key
                almanac_dict[current_almanac_key] = []
            else:
                almanac_string_list = line.split(" ")
                almanac_int_list = [int(x) for x in almanac_string_list]
                almanac_dict[current_almanac_key].append(almanac_int_list)
    return almanac_dict

def find_next_numbers_and_ranges(numbers_to_check, current_numbers_and_ranges):
    numbers_to_check.sort(key=lambda x: x[1])
    new_numbers_and_ranges = []

    for i, [current_number, current_range] in enumerate(current_numbers_and_ranges):
        for j, [number_to_return, number_to_check, range_to_check] in enumerate(numbers_to_check):
            
            if current_number > number_to_check + range_to_check - 1:
                if i + 1 == len(current_numbers_and_ranges) and j + 1 == len(numbers_to_check):
                    new_numbers_and_ranges.append([current_number, current_range])
                continue
            
            elif current_number < number_to_check:
                if current_number + current_range - 1 <= number_to_check:
                    new_numbers_and_ranges.append([current_number, current_range])
                    break
                else:
                    valid_numbers = number_to_check - current_number 
                    new_numbers_and_ranges.append([current_number, valid_numbers])
                    current_numbers_and_ranges.insert(i + 1, [current_number + valid_numbers + 1, current_range - valid_numbers])
                    break
                    
            elif current_number >= number_to_check:
                if current_number + current_range - 1 <= number_to_check + range_to_check:
                    difference = current_number - number_to_check 
                    new_numbers_and_ranges.append([number_to_return + difference, current_range])
                    break
                else:
                    valid_numbers = (number_to_check + range_to_check) - current_number
                    difference = current_number - number_to_check 
                    new_numbers_and_ranges.append([number_to_return + difference, valid_numbers])
                    current_numbers_and_ranges.insert(i + 1, [current_number + valid_numbers, current_range - valid_numbers])
                    break
    return new_numbers_and_ranges

def get_lowest_location(seed_location_list):
    lowest_seed = 0
    for seed, _ in seed_location_list:
        if not lowest_seed:
            lowest_seed = seed
        if seed < lowest_seed:
            lowest_seed = seed 
    return lowest_seed

def find_lowest_location_for_seed(almanac_dict):
    seeds_to_check_list = almanac_dict["seeds"]
    process_list = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    seed_location_list = []
    for seed, seed_range in seeds_to_check_list:
        current_numbers_and_ranges = [[seed, seed_range]]
        for process in process_list:
            numbers_to_check = almanac_dict[process]
            current_numbers_and_ranges = find_next_numbers_and_ranges(numbers_to_check, current_numbers_and_ranges)
        seed_location_list.extend(current_numbers_and_ranges)
    return get_lowest_location(seed_location_list)

raw_almanac = read_input()
almanac_dict = raw_almanac_to_almanac_dict(raw_almanac)
result = find_lowest_location_for_seed(almanac_dict)
print(result)