from reader import read_problem

digit_with_letters = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def has_digit_with_letters(str):
    for digit in digit_with_letters:
        if digit == str[:len(digit)]:
            return digit
        
    return False

def getValue(digit):
    if digit.isnumeric():
        return digit
    else:
        return digit_with_letters[digit]


def main():
    content = read_problem("input.txt")
    total_calibration_values = 0
    for line in content:
        digits = []
        for i in range(len(line)):
            if line[i].isnumeric():
                digits.append(line[i])
            else:
                value = has_digit_with_letters(line[i:-1])
                if value:
                    digits.append(value)
                    i += len(value)

        total_calibration_values += int(getValue(digits[0]) + getValue(digits[-1]))

    print("Total clalibration value is: ", total_calibration_values)
main()