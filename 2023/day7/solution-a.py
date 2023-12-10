import operator as op
from collections import Counter

input_file = open("input-example.txt")

content = input_file.readlines()

input_file.close()

hands = []

for line in content:
    hands.append({"hand": list(line.split()[0]), "bid": int(line.split()[1]) })


def get_number_of_same_cards(hand):
    print(hand)
    temp_hand = hand
    counter_map = {}
    for i in range(len(hand)):
        temp_counter = op.countOf(temp_hand, hand[i])
        counter_map[hand[i]] = temp_counter
        list(filter((hand[i]).__ne__, temp_hand))

    return counter_map

def find_type(hand):
    temp_hand = hand
    counter_map = get_number_of_same_cards(hand)
    if 5 in counter_map.values():
        return "Five of a kind"
    elif 4 in counter_map.values():
        return "Five of a kind"
    elif 3 in counter_map.values():
        for k in counter_map:
            if counter_map[k] == 3:
                temp_hand = list(filter(("3").__ne__, temp_hand))
        if len(temp_hand) > 1 and temp_hand[0] != temp_hand[1]:
            return "Three of a kind"
        else:
            return "Full house"
        
    elif 2 in counter_map.values():
        return "Five of a kind"

    print(counter_map)

print(find_type(hands[0]["hand"]))