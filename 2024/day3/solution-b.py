from reader import read_problem
import re 

def multiply(exp):
    digits = re.findall("\d{1,3}", exp)
    res = int(digits[0]) * int(digits[1])
    return res

def find_multiplies(exp):
    multiplies = re.findall("mul\(\d{1,3},\d{1,3}\)", exp)
    sum = 0
    for m in multiplies:
        sum += multiply(m)

    return sum

def main():
    lines = read_problem("input.txt")

    content = ""
    for l in lines:
        content += l

    # do().*?don't()

    content = content.replace("\n", "")
    sum = 0
    matches_first_part = re.findall("(^.*?(do\(\)|don\'t\(\)))", content)

    if len(matches_first_part) > 0:
        sum += find_multiplies(matches_first_part[0][0])
    matches_do = re.findall("do\(\).*?don\'t\(\)", content)
   

    for match in matches_do:
        sum += find_multiplies(match)

    print("sum => ", sum)

main()