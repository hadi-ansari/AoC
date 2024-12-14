from reader import read_problem

X = 0
Y = 1

POS_IDX = 0
VELOCITY_IDX = 1

def draw_map(map_size, robots):
    for y in range(map_size[Y]):
        line = ""
        for x in range(map_size[X]):
            robot_counter = 0
            for r in robots:
                if r[POS_IDX] == (x, y):
                    robot_counter += 1
            if robot_counter > 0:
                line += str(robot_counter)
            else:
                line += "."

        print(line)
    print()

def calculate_total(map_size, robots):
    middle_x_idx = map_size[X] // 2
    middle_y_idx = map_size[Y] // 2

    quarter_one_total = 0
    quarter_two_total = 0
    quarter_three_total = 0
    quarter_four_total = 0

    for r in robots:
        if r[POS_IDX][X] in range(0, middle_x_idx) and r[POS_IDX][Y] in range(0, middle_y_idx):
            quarter_one_total += 1
        elif r[POS_IDX][X] in range(middle_x_idx + 1, map_size[X]) and r[POS_IDX][Y] in range(0, middle_y_idx):
            quarter_two_total += 1
        elif r[POS_IDX][X] in range(0, middle_x_idx) and r[POS_IDX][Y] in range(middle_y_idx + 1, map_size[Y]):
            quarter_three_total += 1
        elif r[POS_IDX][X] in range(middle_x_idx + 1, map_size[X]) and r[POS_IDX][Y] in range(middle_y_idx + 1, map_size[Y]):
            quarter_four_total += 1

    return quarter_one_total * quarter_two_total * quarter_three_total * quarter_four_total


def tick(map_size, robots):
    new_robots = []
    for r in robots:
        new_x_pos = r[POS_IDX][X] + r[VELOCITY_IDX][X]
        new_y_pos = r[POS_IDX][Y] + r[VELOCITY_IDX][Y]

        if new_x_pos < 0:
            new_x_pos = map_size[X] + (r[POS_IDX][X] + r[VELOCITY_IDX][X])

        if new_x_pos >= map_size[X]:
            new_x_pos = (r[POS_IDX][X] + r[VELOCITY_IDX][X]) - map_size[X]

        if new_y_pos < 0:
            new_y_pos = map_size[Y] + (r[POS_IDX][Y] + r[VELOCITY_IDX][Y])

        if new_y_pos >= map_size[Y]:
            new_y_pos = (r[POS_IDX][Y] + r[VELOCITY_IDX][Y]) - map_size[Y]

        new_robots.append(((new_x_pos, new_y_pos), r[VELOCITY_IDX]))

    return new_robots

def main():
    robots, map_size = read_problem("input.txt")
    sum = 0

    for i in range(100):
        robots = tick(map_size, robots)

    sum = calculate_total(map_size, robots)
    
    print("sum is => ", sum)

main()