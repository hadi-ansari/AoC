from reader import read_problem

def main():
    races = read_problem("input.txt")

    time = ""
    distance = ""
    for i in range(len(races)):
        time += str(races[i][0])
        distance += str(races[i][1])
    time = int(time)
    distance = int(distance)

    possible_count = 0
    for j in range(1, time - 1):
        speed = j
        temp_dis = speed * (time - j)
        if temp_dis > distance:
            possible_count += 1


    print("Answer is {}".format(possible_count))
    
main()