from reader import read_problem


def main():
    bag_config = (12, 13, 14)
    possible_games_ids = []
    games = read_problem("input.txt")
    for i in range(len(games)):
        possible_game = True
        for subset in games[i]:
            if subset[0] > bag_config[0] or subset[1] > bag_config[1] or subset[2] > bag_config[2]:
                possible_game = False
                break
        if possible_game:
            possible_games_ids.append(i + 1)

    sum = 0
    for game_id in possible_games_ids:
        sum += game_id

    print(sum)
    return


main()