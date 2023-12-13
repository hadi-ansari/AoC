from reader import read_problem

def main():
    game_powers = []
    games = read_problem("input.txt")
    for i in range(len(games)):
        max_red_in_game = max(list(map(lambda p: p[0], list(map(lambda v: v, games[i])))))
        max_green_in_game = max(list(map(lambda p: p[1], list(map(lambda v: v, games[i])))))
        max_blue_in_game = max(list(map(lambda p: p[2], list(map(lambda v: v, games[i])))))
        # print("game set is {} and \nmax red is: {}\nmax green is: {}\nmax blue is: {}".format(games[i], max_red_in_game, max_green_in_game, max_blue_in_game))
      
        game_powers.append(max_red_in_game * max_green_in_game * max_blue_in_game)

    sum = 0
    for power in game_powers:
        sum += power

    print(sum)
    return


main()