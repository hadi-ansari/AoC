from reader import read_problem

def main():
    content = read_problem("input.txt")
    total_value = 0
    for line in content:
        first_digit = False
        second_digit = False
        for c in line:
            if c.isnumeric():
                if not first_digit:
                    first_digit = c
                else:
                    second_digit = c
        if not second_digit:
            second_digit = first_digit
        total_value += int(first_digit + second_digit)
        
    print(total_value)

main()