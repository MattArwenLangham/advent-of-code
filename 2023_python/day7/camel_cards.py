import re

def read_input():
    f = open("input.txt", "r")
    return f.read().split("\n")

def calculate_rank_of_hand(hand):
    hand_set = set(hand)
    if len(hand_set) == 1:
        return '7'
    elif len(hand_set) == 2:
        for value in hand_set:
            if hand.count(value) == 4:
                return '6'
        return '5'
    elif len(hand_set) == 3:
        for value in hand_set:
            if hand.count(value) == 3:
                return '4'
        return '3'
    elif len(hand_set) == 4:
        return '2'
    elif len(hand_set) == 5:
        return '1'
    
def calculate_strength_of_hand(hand):
    values = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
    hand_strength = re.sub(r'(\d)', r'0\1', hand)
    for value, strength in values.items():
        hand_strength = hand_strength.replace(value, strength)
    return hand_strength

def calculate_ranks_of_hands(hands_and_bets):
    weightings_and_bets = []  
    for hand_and_bet in hands_and_bets:
        hand, bet = hand_and_bet.split(" ")
        rank = calculate_rank_of_hand(hand)
        strength = calculate_strength_of_hand(hand)
        final_weighting = int(rank + strength)
        weigthing_and_bet = [final_weighting, int(bet)]
        weightings_and_bets.append(weigthing_and_bet)
    return weightings_and_bets

def calculate_total_winnings(weightings_and_bets):
    weightings_and_bets.sort(key=lambda x: x[0])
    total_winnings = 0
    for rank, [_, bet] in enumerate(weightings_and_bets):
        total_winnings += bet * (rank + 1)
    return total_winnings


hands_and_bets = read_input()
weightings_and_bets = calculate_ranks_of_hands(hands_and_bets)
result = calculate_total_winnings(weightings_and_bets)
print(result)