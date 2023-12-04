import re

def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

def find_num_of_wins(winning_numbers, numbers_to_check):
    winning_number_list = winning_numbers.strip(" ").replace("  ", " ").split(" ")
    numbers_to_check_list = numbers_to_check.strip(" ").replace("  ", " ").split(" ")
    numbers_won_set = set(numbers_to_check_list).intersection(winning_number_list)
    return int(len(numbers_won_set))

def add_scratchcards_to_dict(scratchcards):
    scratchcards_dict = {
    }

    for scratchcard in scratchcards:
        card, winning_numbers, numbers_to_check = re.split(':|\|', scratchcard)
        num_of_wins = find_num_of_wins(winning_numbers, numbers_to_check)
        card_number = int(card[5:])
        scratchcards_dict[card_number] = [num_of_wins, 1]
    
    return scratchcards_dict

def calculate_num_of_scratchcards_used(scratchcards_dict):
    num_of_scratchcards_used = 0
    for card_num, [wins, quantity] in scratchcards_dict.items():
        num_of_scratchcards_used += quantity
        for i in range(1, wins + 1):
            scratchcards_dict[card_num + i][1] += 1 * quantity
    
    return num_of_scratchcards_used

scratchcards = read_input()
scratchcards_dict = add_scratchcards_to_dict(scratchcards)
result = calculate_num_of_scratchcards_used(scratchcards_dict)
print(result)