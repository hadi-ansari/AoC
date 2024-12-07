from reader import read_problem
from itertools import product


def find_product(list):
    total_operations_possible = len(list[1]) - 1
    pro = product(["+", "*"], repeat=total_operations_possible)
   
    return pro

def is_true(list, pro):
    for p in pro:
        i = 0
        sum = int(list[1][i])
        for op in p:
            if op == "*":
                sum *= int(list[1][i +1])

            elif op == "+":
                sum += int(list[1][i +1])
            i+=1
        
        if sum == int(list[0]):
            return True
    
    return False

def main():
    equations = read_problem("input.txt")
    sum = 0
    for e in equations:
        p = find_product(e)
        if is_true(e, p):
            sum += int(e[0])

    print("sum => ", sum)
 

main()