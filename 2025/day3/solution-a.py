from reader import read_problem


def find_max_joltage(bank):
    max_first_digit = -1
    max_second_digit = -1
    max_index = -1

    for i in range(len(bank) - 1):
        if int(bank[i]) > max_first_digit:
            max_first_digit = int(bank[i])
            max_index = i

    for j in range(max_index + 1, len(bank)):
        if int(bank[j]) > max_second_digit:
            max_second_digit = int(bank[j])
            max_index_second = j


    return int(str(max_first_digit) + str(max_second_digit))


def main():
    banks = read_problem("input.txt")
    sum = 0
    for bank in banks:
        max_joltage = find_max_joltage(bank)
        sum += max_joltage

    print("The sum of max joltage is:", sum)

main()