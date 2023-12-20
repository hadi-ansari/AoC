from reader import read_problem
import copy

def main():
    sequences = read_problem("input.txt")
    sum_of_extrapolation = 0
    for seq in sequences:
        diff = (seq[-1] - seq[-2])  - (seq[-2] - seq[-3])
        init_fixed = (seq[1] - seq[0])
        extrapolation = 0
        # print("Init diff:{}, diff factor: {}".format(init_fixed, diff))
        # print(extrapolation)
        temp = copy.deepcopy(seq)
        temp2 = []
        lasts = []
        while True:
            lasts.append(temp[-1])
            for i in range(0, len(temp) - 1):
                temp2.append(temp[i + 1] - temp[i])


            # print("new list => ", temp2)
            if len(set(temp2)) == 1 and temp2[0] == 0:
                break
            
            temp = copy.deepcopy(temp2)
            temp2 = []

        # print("lasts => ", lasts)
        for l in lasts:
            extrapolation += l

        
        sum_of_extrapolation += extrapolation

        # print("=" * 50)
    print(sum_of_extrapolation)

main()