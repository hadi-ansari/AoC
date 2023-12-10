from reader import read_problem

def main():
    cards = read_problem("input.txt")
    total_points = 0

    formated_cards = []
    for card in cards:
        winning_numbers = card[0]
        owned_numbers = card[1]
        formated_cards.append([winning_numbers, owned_numbers])

    for formated_card in formated_cards:
        temp_point = 0
        for winning_number in formated_card[0]:
            for owned_number in formated_card[1]:
                if winning_number == owned_number:
                    if temp_point == 0:
                        temp_point+=1
                    else:
                        temp_point*=2
        total_points += temp_point


    print("Total point is: ", total_points)

main()