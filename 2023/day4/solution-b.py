from reader import read_problem

def get_number_of_matches(card):
    number_of_matches = 0
    for i in card[0]:
        if i in card[1]:
            number_of_matches += 1

    return number_of_matches


def main():
    cards = read_problem("input.txt")

    for i in range(len(cards)):
        steps = get_number_of_matches(cards[i])
        for c in range(cards[i][2]):
            if i + steps > len(cards):
                steps = len(cards) - i 
            for j in range(i + 1, i + 1 + steps):
                cards[j][2] += 1

    total_scratch_cards = 0
    for i in range(len(cards)):
        total_scratch_cards += cards[i][2]

    print("Total scratch cards:", total_scratch_cards)

main()