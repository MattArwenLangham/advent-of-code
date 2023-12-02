import re

def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

possible_cube_quantity = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def is_round_possible(round):
    turns = [turn.split(" ") for turn in round.split(", ")]

    for cube_quantity, cube_colour in turns:
        if possible_cube_quantity.get(cube_colour) < int(cube_quantity):
            return False
    
    return True

def are_rounds_possible(rounds):
    return all(is_round_possible(round) for round in rounds)

def analyse_games(games_list):
    possible_games = []

    for game in games_list:
        game_id, *rounds = re.split(': |; ', game)
        game_id_int = int(game_id.split(" ")[1])

        if are_rounds_possible(rounds):
            possible_games.append(game_id_int)
    
    return sum(possible_games)

games_list = read_input()
print(analyse_games(games_list))