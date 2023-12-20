from reader import read_problem
import copy

def main():
    sequences = read_problem("input.txt")
    sum_of_extrapolation = 0
    for seq in sequences:
        # print("Init diff:{}, diff factor: {}".format(init_fixed, diff))
        temp1 = copy.deepcopy(seq)
        temp2 = []
        firsts = []
        while True:
            firsts.append(temp1[0])
            for i in range(0, len(temp1) - 1):
                temp2.append(temp1[i + 1] - temp1[i])


            if len(set(temp2)) == 1 and temp2[0] == 0:
                break
            
            temp1 = copy.deepcopy(temp2)
            temp2 = []

        firsts.reverse()
        extrapolation = firsts[0]
        for i in range(1, len(firsts)):
            extrapolation = firsts[i] - extrapolation

        sum_of_extrapolation += extrapolation

    print(sum_of_extrapolation)

main()