from reader import read_problem
from enum import Enum
import copy
import os

X = 0
Y = 1

class DIRS(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"

UP_IDX = -1
RIGHT_IDX = 1
DOWN_IDX = 1
LEFT_IDX = -1

def exist(map, dir, pos, char):
    if dir == "^":
        if pos[Y] > 0 and map[pos[Y] + UP_IDX][pos[X]] == char:
            return True
    elif dir == ">":
        if pos[X] < len(map[0]) - 1 and map[pos[Y]][pos[X] + RIGHT_IDX] == char:
            return True
    elif dir == "v":
        if pos[Y] < len(map) - 1 and map[pos[Y] + DOWN_IDX][pos[X]] == char:
            return True
    elif dir == "<":
        if pos[X] > 0 and map[pos[Y]][pos[X] + LEFT_IDX] == char:
            return True
      
    return False


# pos is always positon of "[" in the box
def move_box(map, dir, pos):
    new_map = copy.deepcopy(map)
    new_pos = pos

    if dir == "^":
        new_map[pos[Y]][pos[X]] = "."
        new_map[pos[Y]][pos[X] + RIGHT_IDX] = "."
        new_map[pos[Y] + UP_IDX][pos[X]] = "["
        new_map[pos[Y] + UP_IDX][pos[X] + RIGHT_IDX] = "]"
    elif dir == ">":
        new_map[pos[Y]][pos[X]] = "."
        new_map[pos[Y]][pos[X] + RIGHT_IDX] = "["
        new_map[pos[Y]][pos[X] + RIGHT_IDX * 2] = "]"
    elif dir == "v":
        new_map[pos[Y]][pos[X]] = "."
        new_map[pos[Y]][pos[X] + RIGHT_IDX] = "."
        new_map[pos[Y] + DOWN_IDX][pos[X]] = "["
        new_map[pos[Y] + DOWN_IDX][pos[X] + RIGHT_IDX] = "]"
    elif dir == "<":
        new_map[pos[Y]][pos[X] + RIGHT_IDX] = "."
        new_map[pos[Y]][pos[X]] = "]"
        new_map[pos[Y]][pos[X] + LEFT_IDX] = "["

    return new_map, new_pos


def move_robot(map, dir, pos):
    new_map = copy.deepcopy(map)
    new_pos = pos
    new_map[pos[Y]][pos[X]] = "."

    if dir == "^":
        new_map[pos[Y] + UP_IDX][pos[X]] = "@"
        new_pos = (pos[X], pos[Y] + UP_IDX)

    elif dir == ">":
        new_map[pos[Y]][pos[X] + RIGHT_IDX] = "@"
        new_pos = (pos[X] + RIGHT_IDX, pos[Y])

    elif dir == "v":
        new_map[pos[Y] + DOWN_IDX][pos[X]] = "@"
        new_pos = (pos[X], pos[Y] + DOWN_IDX)
    elif dir == "<":
        new_map[pos[Y]][pos[X] + LEFT_IDX] = "@"
        new_pos = (pos[X] + LEFT_IDX, pos[Y])
    
    return new_map, new_pos  

def tick(map, instruction, pos):
    success = False
    new_map = copy.deepcopy(map)
    if map[pos[Y]][pos[X]] == "]":
        pos = (pos[X] - 1, pos[Y])


    curr_value = map[pos[Y]][pos[X]]
    new_pos = pos
    box_moving = False
    if curr_value == "[" or curr_value == "]":
        box_moving = True


    if instruction == "^":
        if not box_moving:
            if exist(map, instruction, pos, "."):
                new_map, new_pos = move_robot(map, instruction, new_pos)
            elif exist(map, instruction, pos, "[") or exist(map, instruction, pos, "]"):
                sub_success, new_sub_map, new_box_pos = tick(map, instruction, (pos[X], pos[Y] + UP_IDX))
                if sub_success:
                    new_map, new_pos = move_robot(new_sub_map, instruction, new_pos)
                    success = True

        if box_moving:
            free_to_move = exist(map, instruction, pos, ".") and  exist(map, instruction, (pos[X] + RIGHT_IDX, pos[Y]), ".")
            end_box_up = exist(new_map, instruction, pos, "]")
            start_box_up = exist(map, instruction, pos, "[") 
            start_box_up_righ = exist(new_map, instruction, (pos[X] + RIGHT_IDX, pos[Y]), "[")
            up_wall = exist(map, instruction, pos, "#") 
            up_right_wall = exist(map, instruction, (pos[X] + RIGHT_IDX, pos[Y]), "#") 
        
            if free_to_move:
                new_map, _ = move_box(map, instruction, new_pos)
                success = True
            elif up_wall or up_right_wall:
                pass
            elif end_box_up or start_box_up or start_box_up_righ:
                if start_box_up:
                    sub_success, new_sub_map, new_box_pos = tick(map, instruction, (pos[X], pos[Y] + UP_IDX))
                    if sub_success:
                        new_map = new_sub_map
                        new_map, new_pos = move_box(new_sub_map, instruction, new_pos)
                        success = True
                elif end_box_up:
                    if start_box_up_righ:
                        # Two boxes underneath
                        temp_map = copy.deepcopy(new_map)
                        sub_success1, new_sub_map1, new_box_pos1 = tick(temp_map, instruction, (pos[X] + LEFT_IDX, pos[Y] + UP_IDX))
                        sub_success2, new_sub_map2, new_box_pos2 = tick(new_sub_map1, instruction, (pos[X] + RIGHT_IDX, pos[Y] + UP_IDX))
                        if sub_success1 and sub_success2:
                            new_map = new_sub_map2
                            new_map, new_pos = move_box(new_map, instruction, new_pos)
                            success = True
                    else:
                        sub_success1, new_sub_map1, new_box_pos1 = tick(new_map, instruction, (pos[X] + LEFT_IDX, pos[Y] + UP_IDX))
                        if sub_success1:
                            new_map = new_sub_map1
                            new_map, new_pos = move_box(new_map, instruction, new_pos)
                            success = True
                elif start_box_up_righ:
                    sub_success2, new_sub_map2, new_box_pos2 = tick(new_map, instruction, (pos[X] + RIGHT_IDX, pos[Y] + UP_IDX))
                    if sub_success2:
                        new_map = new_sub_map2
                        new_map, new_pos = move_box(new_map, instruction, new_pos)
                        success = True

                

    if instruction == "v":
        if not box_moving:
            if exist(new_map, instruction, pos, "."):
                new_map, new_pos = move_robot(new_map, instruction, new_pos)
            elif exist(new_map, instruction, pos, "[") or exist(new_map, instruction, pos, "]"):
                sub_success, new_sub_map, new_box_pos = tick(new_map, instruction, (pos[X], pos[Y] + DOWN_IDX))
                if sub_success:
                    new_map = new_sub_map
                    new_map, new_pos = move_robot(new_map, instruction, new_pos)
                    success = True

        if box_moving:
            free_to_move = exist(new_map, instruction, pos, ".") and  exist(new_map, instruction, (pos[X] + RIGHT_IDX, pos[Y]), ".")
            end_box_up = exist(new_map, instruction, (pos[X], pos[Y]), "]")
            start_box_up = exist(new_map, instruction, (pos[X], pos[Y]), "[")
            start_box_up_righ = exist(new_map, instruction, (pos[X] + RIGHT_IDX, pos[Y]), "[")
            down_wall = exist(map, instruction, pos, "#") 
            down_righ_wall = exist(map, instruction, (pos[X] + RIGHT_IDX, pos[Y]), "#") 

            if free_to_move:
                new_map, _ = move_box(map, instruction, new_pos)
                success = True
            elif down_wall or down_righ_wall:
                pass
            elif end_box_up or start_box_up or start_box_up_righ:
                if start_box_up:
                    sub_success, new_sub_map, new_box_pos = tick(new_map, instruction, (pos[X], pos[Y] + DOWN_IDX))
                    if sub_success:
                        new_map = new_sub_map
                        new_map, new_pos = move_box(new_map, instruction, new_pos)
                        success = True
                elif end_box_up:
                    if start_box_up_righ:
                        # Two boxes underneath
                        temp_map = copy.deepcopy(new_map)
                        sub_success1, new_sub_map1, new_box_pos1 = tick(temp_map, instruction, (pos[X] + LEFT_IDX, pos[Y] + DOWN_IDX))
                        sub_success2, new_sub_map2, new_box_pos2 = tick(new_sub_map1, instruction, (pos[X] + RIGHT_IDX, pos[Y] + DOWN_IDX))
                        if sub_success1 and sub_success2:
                            new_map = new_sub_map2
                            new_map, new_pos = move_box(new_map, instruction, new_pos)
                            success = True
                    else:
                        sub_success1, new_sub_map1, new_box_pos1 = tick(new_map, instruction, (pos[X] + LEFT_IDX, pos[Y] + DOWN_IDX))
                        if sub_success1:
                            new_map = new_sub_map1
                            new_map, new_pos = move_box(new_map, instruction, new_pos)
                            success = True
                elif start_box_up_righ:
                    sub_success2, new_sub_map2, new_box_pos2 = tick(new_map, instruction, (pos[X] + RIGHT_IDX, pos[Y] + DOWN_IDX))
                    if sub_success2:
                        new_map = new_sub_map2
                        new_map, new_pos = move_box(new_map, instruction, new_pos)
                        success = True

    if instruction == ">":
        if not box_moving:
            if exist(map, instruction, pos, "."):
                new_map, new_pos = move_robot(new_map, instruction, new_pos)
            elif exist(map, instruction, pos, "["):
                sub_success, new_sub_map, new_box_pos = tick(new_map, instruction, (pos[X] + RIGHT_IDX, pos[Y]))
                if sub_success:
                    new_map = new_sub_map
                    new_map, new_pos = move_robot(new_map, instruction, new_pos)
                    success = True

        if box_moving:
            if exist(map, instruction, (pos[X] + RIGHT_IDX, pos[Y]), "."):
                new_map, _ = move_box(map, instruction, new_pos)
                success = True
            elif exist(map, instruction, (pos[X] + RIGHT_IDX * 2, pos[Y]), "]"):
                sub_success, new_sub_map, new_box_pos = tick(map, instruction, (pos[X] + RIGHT_IDX * 2, pos[Y]))
                if sub_success:
                    new_map = new_sub_map
                    new_map, new_pos = move_box(new_sub_map, instruction, new_pos)
                    success = True

    if instruction == "<":
        if not box_moving:
            if exist(map, instruction, pos, "."):
                new_map, new_pos = move_robot(new_map, instruction, new_pos)
            elif exist(map, instruction, pos, "]"):
                sub_success, new_sub_map, new_box_pos = tick(new_map, instruction, (pos[X] + LEFT_IDX * 2, pos[Y]))
                if sub_success:
                    new_map = new_sub_map
                    new_map, new_pos = move_robot(new_map, instruction, new_pos)
                    success = True

        if box_moving:
            if exist(map, instruction, pos, "."):
                new_map, _ = move_box(map, instruction, new_pos)
                success = True
            elif exist(map, instruction, pos, "]"):
                sub_success, new_sub_map, new_box_pos = tick(map, instruction, (pos[X] + LEFT_IDX * 2, pos[Y]))
                if sub_success:
                    new_map = new_sub_map
                    new_map, new_pos = move_box(new_sub_map, instruction, new_pos)
                    success = True
   

    return success, new_map, new_pos

def draw_map(map):
    for y in range(len(map)):
        line = ""
        for x in range(len(map[y])):
            line += map[y][x] + " " # Just for better looking
        
        print(line)

    print()

def calculate_box_coordinates(map):
    sum = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "[":
                sum += 100 * y + x
    return sum

def change_map(map):
    new_map = []

    for y in range(len(map)):
        line = []
        for x in range(len(map[y])):
            if map[y][x] == "@":
                line.append("@")
                line.append(".",)
            elif map[y][x] == "#":
                line.append("#")
                line.append("#")
            elif map[y][x] == ".":
                line.append(".")
                line.append(".")
            elif map[y][x] == "O":
                line.append("[")
                line.append("]")
        new_map.append(line)

    return new_map
    
def main():
    map, instructions = read_problem("input.txt")
    sum = 0

    robot_pos = (-1, -1)

    new_map = change_map(map)
    for y in range(len(new_map)):
        for x in range(len(new_map[y])):
            if new_map[y][x] == "@":
                robot_pos = (x, y)
                break
            
    for i in range(len(instructions)):
        success, new_map, robot_pos = tick(new_map, instructions[i], robot_pos)

    sum = calculate_box_coordinates(new_map)
    
    print("sum is => ", sum)

    ##############################################
    # UNCOMMENT THISSECTION FOR ENTERING
    # GAME MODE! 
    ##############################################
    # draw_map(new_map)
    # while True:
    #     input_value = input("Enter instruction: \t")
    #     print(input_value)
    #     if input_value == "w":
    #         input_value = "^"
    #     if input_value == "d":
    #         input_value = ">"
    #     if input_value == "s":
    #         input_value = "v"
    #     if input_value == "a":
    #         input_value = "<"

    #     if input_value == "^" or input_value == "v" or input_value == ">" or input_value == "<":
    #         success, new_map, robot_pos = tick(new_map, input_value, robot_pos)
    #     os.system('clear')
    #     draw_map(new_map)

main()