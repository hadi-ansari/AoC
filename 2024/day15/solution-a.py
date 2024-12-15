from reader import read_problem
import copy

X = 0
Y = 1

UP_IDX = -1
RIGHT_IDX = 1
DOWN_IDX = 1
LEFT_IDX = -1

def move(map, instruction, pos):
    success = False
    curr_value = map[pos[Y]][pos[X]]
    new_map = copy.deepcopy(map)
    new_pos = pos

    if instruction == "^" and new_map[pos[Y] + UP_IDX][pos[X]] == "O":
        success_box, map_box, new_box_pos = move(new_map, instruction, (pos[X], pos[Y] + UP_IDX))
        if success_box:
            new_map = map_box
            new_map[pos[Y]][pos[X]] = "."
            new_map[pos[Y] + UP_IDX][pos[X]]  = curr_value
            success = True
            new_pos = (pos[X], pos[Y] + UP_IDX)

    elif instruction == "^" and new_map[pos[Y] + UP_IDX][pos[X]] == ".":
        new_map[pos[Y]][pos[X]] = "."
        new_map[pos[Y] + UP_IDX][pos[X]] = curr_value
        success = True
        new_pos = (pos[X], pos[Y] + UP_IDX)
        

    elif instruction == ">" and new_map[pos[Y]][pos[X] + RIGHT_IDX] == "O":
        success_box, map_box, ok = move(new_map, instruction, (pos[X] + RIGHT_IDX, pos[Y]))
        if success_box:
            new_map = map_box
            new_map[pos[Y]][pos[X]] = "."
            new_map[pos[Y]][pos[X] + RIGHT_IDX] = curr_value
            success = True
            new_pos = (pos[X] + RIGHT_IDX, pos[Y])


    elif instruction == ">" and new_map[pos[Y]][pos[X] + RIGHT_IDX] == ".":
        new_map[pos[Y]][pos[X]] = "."
        new_map[pos[Y]][pos[X] + RIGHT_IDX] = curr_value
        success = True
        new_pos = (pos[X] + RIGHT_IDX, pos[Y])


    elif instruction == "v" and new_map[pos[Y] + DOWN_IDX][pos[X]] == "O":
        success_box, map_box, new_box_pos = move(new_map, instruction, (pos[X], pos[Y] + DOWN_IDX))
        if success_box:
            new_map = map_box
            new_map[pos[Y]][pos[X]] = "."
            new_map[pos[Y] + DOWN_IDX][pos[X]] = curr_value
            success = True
            new_pos = (pos[X], pos[Y] + DOWN_IDX)

    elif instruction == "v" and new_map[pos[Y] + DOWN_IDX][pos[X]] == ".":
        new_map[pos[Y]][pos[X]] = "."
        new_map[pos[Y] + DOWN_IDX][pos[X]] = curr_value
        success = True
        new_pos = (pos[X], pos[Y] + DOWN_IDX)


    elif instruction == "<" and new_map[pos[Y]][pos[X] + LEFT_IDX] == "O":
        success_box, map_box, new_box_pos = move(new_map, instruction, (pos[X] + LEFT_IDX, pos[Y]))
        if success_box:
            new_map = map_box
            new_map[pos[Y]][pos[X]] = "."
            new_map[pos[Y]][pos[X] + LEFT_IDX] = curr_value
            success = True
            new_pos = (pos[X] + LEFT_IDX, pos[Y])


    elif instruction == "<" and new_map[pos[Y]][pos[X] + LEFT_IDX] == ".":
        new_map[pos[Y]][pos[X]] = "."
        new_map[pos[Y]][pos[X] + LEFT_IDX] = curr_value
        success = True
        new_pos = (pos[X] + LEFT_IDX, pos[Y])

    return success, new_map, new_pos

def draw_map(map):
    for y in range(len(map)):
        line = ""
        for x in range(len(map[y])):
            line += map[y][x] + " " # Just for better looking
        
        print(line)

    print()

def tick(map, instruction, pos):
    success, new_map, new_robot_pos = move(map, instruction, pos)

    return success, new_map, new_robot_pos

def calculate_box_coordinates(map):
    sum = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "O":
                sum += 100 * y + x
    return sum
def main():
    map, instructions = read_problem("input.txt")
    sum = 0

    robot_pos = (-1, -1)

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "@":
                robot_pos = (x, y)

    for i in range(len(instructions)):
        success, map, robot_pos = tick(map, instructions[i], robot_pos)
    
    draw_map(map)

    sum = calculate_box_coordinates(map)
    
    print("sum is => ", sum)

main()