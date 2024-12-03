from reader import read_problem
import re 

def multiply(exp):
    digits = re.findall("\d{1,3}", exp)
    res = int(digits[0]) * int(digits[1])
    return res

def main():
    curropted_memory = read_problem("input.txt")

    sum = 0

    for line in curropted_memory:
        matches = re.findall("mul\(\d{1,3}\,\d{1,3}\)", line)
        for match in matches:
            sum += multiply(match)

    print("sum => ", sum)

main()