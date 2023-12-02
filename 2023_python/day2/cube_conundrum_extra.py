from functools import reduce
from operator import mul
import re

def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

def get_cube_power_of_game(rounds):
    minimum_cubes_possible = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    
    for round in rounds:
        turns = [turn.split(" ") for turn in round.split(", ")]
        for cube_quantity, cube_colour in turns:
            if minimum_cubes_possible.get(cube_colour) < int(cube_quantity):
                minimum_cubes_possible[cube_colour] = int(cube_quantity)

    minimum_quantities = list(minimum_cubes_possible.values())
    return reduce(mul, minimum_quantities, 1)

def analyse_games(games_list):
    cube_powers = []

    for game in games_list:
        _, *rounds = re.split(': |; ', game)
        cube_powers.append(get_cube_power_of_game(rounds))
    
    return sum(cube_powers)

games_list = read_input()
print(analyse_games(games_list))