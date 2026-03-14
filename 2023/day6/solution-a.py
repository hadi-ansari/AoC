from reader import read_problem

def main():
    races = read_problem("input.txt")
    result = 1

    for i in range(len(races)):
        time = races[i][0]
        distance = races[i][1]
        possible_count = 0
        for j in range(1, time - 1):
            speed = j
            temp_dis = speed * (time - j)
            if temp_dis > distance:
                possible_count += 1

        result *= possible_count

    print("Answer is {}".format(result))
    
main()