import operator as op
from reader import read_problem

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

rank_map = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}

def get_number_of_same_cards(hand):
    temp_hand = hand

    counter_map = {}
    for i in range(len(hand)):
        temp_counter = op.countOf(temp_hand, hand[i])
        counter_map[hand[i]] = temp_counter

    return counter_map

def make_strongest_card_possible(hand):
    counter_map = get_number_of_same_cards(hand)

    if(counter_map["J"] == 1):
        if 4 in counter_map.values():
            return FIVE_OF_A_KIND
        elif 3 in counter_map.values():
            return FOUR_OF_A_KIND
        elif 2 in counter_map.values() and list(counter_map.values()).count(2) == 2:
            return FULL_HOUSE
        elif 2 in counter_map.values() and list(counter_map.values()).count(2) == 1:
            return THREE_OF_A_KIND
        else:
            return ONE_PAIR
        
    elif(counter_map["J"] == 2):
        if 3 in counter_map.values():
            return FIVE_OF_A_KIND
        elif 2 in counter_map.values() and list(counter_map.values()).count(2) == 2:
            return FOUR_OF_A_KIND
        else:
            return THREE_OF_A_KIND
        
    elif (counter_map["J"] == 3):
        if 2 in counter_map.values():
            return FIVE_OF_A_KIND
        else:
            return THREE_OF_A_KIND
        
    # 4 or 5 J in hand
    else:
        return FIVE_OF_A_KIND
    
def find_type(hand):
    if "J" in hand:
        return make_strongest_card_possible(hand)
    
    counter_map = get_number_of_same_cards(hand)

    if 5 in counter_map.values():
        return FIVE_OF_A_KIND
    elif 4 in counter_map.values():
        return FOUR_OF_A_KIND
    elif 3 in counter_map.values() and 2 not in counter_map.values():
        return THREE_OF_A_KIND
    elif 3 in counter_map.values():
        return FULL_HOUSE   
    elif 2 in counter_map.values() and list(counter_map.values()).count(2) == 2:
        return TWO_PAIR
    elif 2 in counter_map.values() and list(counter_map.values()).count(2) == 1:
        return ONE_PAIR
    else:
        return HIGH_CARD
    
def sort_func(st):
    offset = 100 ** 5
    sum = 0
    for c in st:
        sum += (rank_map[c] * offset)
        offset //= 100

    return sum
    
def sort_same_types(i, hands):
    same_types = list(filter(lambda x: x[0] == i, hands))
    same_types.sort(key=lambda x: sort_func(x[1]))

    return same_types

def rank_hands(hands):
    hands.sort(key=lambda x: x[0])
    hands.reverse()

    final_sorted_hands = []

    for i in range(1, 8):
        temp = sort_same_types(i, hands)
        final_sorted_hands.append(temp)

    final_sorted_hands = [
            x
            for xs in final_sorted_hands
            for x in xs
        ]
    final_sorted_hands.reverse()
            
    return final_sorted_hands
    
def print_type(num):
    if num == FIVE_OF_A_KIND:
        print("FIVE OF A KIND")
    elif num == FOUR_OF_A_KIND:
        print("FOUR OF A KIND")
    elif num == FULL_HOUSE:
        print("FULL HOUSE")
    elif num == THREE_OF_A_KIND:
        print("THREE OF A KIND")
    elif num == TWO_PAIR:
        print("TWO PAIR")
    elif num == ONE_PAIR:
        print("ONE PAIR")
    elif num == HIGH_CARD:
        print("HIGH CARD")

    
def main():
    hands = read_problem("input.txt")
    typed_hands = []

    for hand in hands:
        typed_hands.append((find_type(hand[0]), hand[0], hand[1]))

    
    ranked_hands = rank_hands(typed_hands)
    ranked_hands.reverse()    
    sum = 0
    for i in range(len(ranked_hands)):
        sum += ((i + 1) * ranked_hands[i][2])

    print(sum)


main()