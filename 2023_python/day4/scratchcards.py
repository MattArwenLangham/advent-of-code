import re

def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

def calculate_numbers_won(numbers_won_set):
    numbers_won_sum = 0

    for _ in numbers_won_set:
        if not numbers_won_sum:
            numbers_won_sum += 1
        else:
            numbers_won_sum *= 2

    return numbers_won_sum

def find_winning_numbers(winning_numbers, numbers_to_check):
    winning_number_list = winning_numbers.strip(" ").replace("  ", " ").split(" ")
    numbers_to_check_list = numbers_to_check.strip(" ").replace("  ", " ").split(" ")
    numbers_won_set = set(numbers_to_check_list).intersection(winning_number_list)

    if not numbers_won_set:
        return 0
    else:
        return calculate_numbers_won(numbers_won_set)

def calculate_sum_of_scratchcards(scratchcards):
    sum_of_scratchcards = 0
    for scratchcard in scratchcards:
        _, winning_numbers, numbers_to_check = re.split(':|\|', scratchcard)
        sum_of_scratchcards += find_winning_numbers(winning_numbers, numbers_to_check)
    
    return sum_of_scratchcards

scratchcards = read_input()
result = calculate_sum_of_scratchcards(scratchcards)
print(result)