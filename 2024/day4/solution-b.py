from reader import read_problem
import re 

def find_MAS(exp):
    result = re.findall("MAS", exp)
    return len(result) > 0

def is_XMAS(lines, i, j):
    if i + 1 >= len(lines) or j + 1 >= len(lines[0]) or i - 1 < 0 or j - 1 < 0:
        return False
    
    ltr = lines[i - 1][j - 1] + lines[i][j] + lines[i + 1][j + 1]
    rtl = lines[i + 1][j - 1] + lines[i][j] + lines[i - 1][j + 1]

    return (find_MAS(ltr) or find_MAS(ltr[::-1])) and (find_MAS(rtl) or find_MAS(rtl[::-1]))

def main():
    lines = read_problem("input.txt")

    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            curr = lines[i][j]
            if curr == "A" and is_XMAS(lines, i, j):
                sum += 1

    
    print("sum => ", sum)

main()