from reader import read_problem

def find_asterisks(line, y):
    found_asterisks = []

    for x in range(len(line)):
        if line[x] == "*":
            found_asterisks.append((x, y))
    
    return found_asterisks

def find_numbers(schematic, y):
    found_numbers = []
    temp_num = ""
    num_start = False
    line_to_search_idx = [y]
    if y > 0:
        line_to_search_idx.append(y - 1)
    if y < len(schematic) - 1:
        line_to_search_idx.append(y + 1)

    for idx in line_to_search_idx:
        for i in range(len(schematic[idx])):
            if num_start and i == len(schematic[idx]) - 1 and schematic[idx][i].isdigit():
                temp_num += schematic[idx][i]
                found_numbers.append((i - len(temp_num) + 1, i, temp_num, idx))
            elif not num_start and i == len(schematic[idx]) - 1 and schematic[idx][i].isdigit():
                temp_num += schematic[idx][i]
                found_numbers.append((i, i, schematic[idx][i], idx))
            elif schematic[idx][i].isdigit():
                num_start = True
            elif not schematic[idx][i].isdigit() and num_start:
                found_numbers.append((i - len(temp_num) , i - 1, temp_num, idx))
                temp_num = ""
                num_start = False

            if num_start:
                temp_num += schematic[idx][i]

    return found_numbers


def is_neighbour(a, p):
    if abs(a[0] - p[0]) <= 1:
        return True
    return False

def is_adjacent_to_num(a, n):
    for x in range(len(n[2])):
        if is_neighbour(a, (x + n[0], n[3])):
            return True
    return False

def main():
    content = read_problem("input.txt")
    schematic = []
    for line in content:
        schematic.append(line.strip())

    gear_ratios = []
    sum = 0

    for i in range(len(schematic)):
        asterisks = find_asterisks(schematic[i], i)
        possible_numbers = []
        if len(asterisks) > 0:
            possible_numbers = find_numbers(schematic, i)
        if len(possible_numbers) > 0:
            for a in asterisks:
                adjacent_nums = []
                for p in possible_numbers:
                    res = is_adjacent_to_num(a, p)
                    if res:
                        adjacent_nums.append(int(p[2]))
                if len(adjacent_nums) == 2:
                    gear_ratio = 1
                    for a in adjacent_nums:
                        gear_ratio *= a
                    gear_ratios.append(gear_ratio)

    for r in gear_ratios:
        sum += r
    print("sum is ", sum)
    return

main()