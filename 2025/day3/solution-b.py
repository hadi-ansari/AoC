from reader import read_problem


def find_max_joltage(bank):
    index = 0
    res = ""

    for c in range(12, 0, -1):
        max_digit = -1
        for i in range(index, len(bank) - c + 1):
            if int(bank[i]) > max_digit:
                max_digit = int(bank[i])
                index = i + 1
        res += str(max_digit)

    return int(res)


def main():
    banks = read_problem("input.txt")
    sum = 0
    for bank in banks:
        max_joltage = find_max_joltage(bank)
        # print("Max joltage for bank", bank, "is", max_joltage)
        sum += max_joltage

    print("The sum of max joltage is:", sum)

main()