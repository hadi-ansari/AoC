from reader import read_problem

def find_numbers(line):
    found_numbers = []
    temp_num = ""
    num_start = False
    for i in range(len(line)):
        if num_start and i == len(line) - 1 and line[i].isdigit():
            temp_num += line[i]
            found_numbers.append((i - len(temp_num) + 1, i, temp_num))
        elif not num_start and i == len(line) - 1 and line[i].isdigit():
            temp_num += line[i]
            found_numbers.append((i, i, line[i]))
        elif line[i].isdigit():
            num_start = True
        elif not line[i].isdigit() and num_start:
            found_numbers.append((i - len(temp_num) , i - 1, temp_num))
            temp_num = ""
            num_start = False

        if num_start:
            temp_num += line[i]

    return found_numbers



def has_adjacent_symbol(schematic, number, line_idx):
    line_len = len(schematic[0])
    col_len = len(schematic)
    x_start = number[0]
    x_end = number[1]
    y = line_idx

    neighbours = []

    x_neighbour_start = x_start
    x_neighbour_end = x_end

    if x_start > 0:
        x_neighbour_start = x_start - 1
        neighbours.append(schematic[line_idx][x_neighbour_start])
    if x_end < line_len - 1:
        x_neighbour_end = x_end + 1
        neighbours.append(schematic[line_idx][x_neighbour_end])
    if y < col_len - 1:
        neighbours.append(schematic[line_idx + 1][x_neighbour_start: x_neighbour_end + 1])
    if y > 0:
        neighbours.append(schematic[line_idx - 1][x_neighbour_start: x_neighbour_end + 1])

    neighbours = "".join(neighbours)
    
    for c in neighbours:
        if c != "." and not c.isdigit():
            return True
    return False
        

def main():
    content = read_problem("input.txt")
    schematic = []
    for line in content:
        # print(line.strip())
        schematic.append(line.strip())

    sum = 0

    for i in range(len(schematic)):
        found_numbers = find_numbers(schematic[i])
        for n in found_numbers:
            if(has_adjacent_symbol(schematic, n, i)):
                sum += int(n[2])
    
    print("sum is ", sum)
    return


main()