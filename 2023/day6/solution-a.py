from reader import read_problem

def main():
    times, distances = read_problem("input.txt")

    time = int("".join(times))
    distance = int("".join(distances))

    possible_count = 0

    for j in range(1, time):
        speed = j
        temp_dis = speed * (time - j)
        # print("If hold {} ms it get {} millimeter".format(j, temp_dis))
        if temp_dis > distance:
            possible_count += 1

    print(possible_count)

main()