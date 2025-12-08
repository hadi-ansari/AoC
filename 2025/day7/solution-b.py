from reader import read_problem

Y_INDEX = 0
X_INDEX = 1

DOWN = 1
UP = -1
LEFT = -1
RIGHT = 1


cheat_sheet = {}

def draw_manifold(manifold):
    for l in manifold:
       print(l)

def find_s_pos(manifold):
    for y in range(len(manifold)):
        for x in range(len(manifold[y])):
            if manifold[y][x] == "S":
                return (y, x)
            

def is_in_manifold(height, width, pos):
    return pos[X_INDEX] < width and pos[Y_INDEX] < height


def tick(manifold, current_pos, height, width):
    nex_pos = (current_pos[Y_INDEX] + DOWN, current_pos[X_INDEX])
    new_positions = []

    # Last line
    if not is_in_manifold(height, width, nex_pos):
        return new_positions, manifold, False

    if manifold[nex_pos[Y_INDEX]][nex_pos[X_INDEX]] == ".":
        manifold[current_pos[Y_INDEX] + DOWN][current_pos[X_INDEX]] = "|"
        new_positions.append(nex_pos)
        return new_positions, manifold, False

    if manifold[nex_pos[Y_INDEX]][nex_pos[X_INDEX]] == "^":
        right_pos = (current_pos[Y_INDEX] + DOWN, current_pos[X_INDEX] + RIGHT)
        left_pos = (current_pos[Y_INDEX] + DOWN, current_pos[X_INDEX] + LEFT)
        if is_in_manifold(height, width, right_pos):
            manifold[right_pos[Y_INDEX]][right_pos[X_INDEX]] = "|"
            new_positions.append(right_pos)
        if is_in_manifold(height, width, left_pos):
            manifold[left_pos[Y_INDEX]][left_pos[X_INDEX]] = "|"
            new_positions.append(left_pos)
        return new_positions, manifold, True
    
    return new_positions, manifold, False

def get_timelines(manifold, current_pos, height, width):
    nex_pos = (current_pos[Y_INDEX] + DOWN, current_pos[X_INDEX])

    if not is_in_manifold(height, width, nex_pos):
        return 0
    
    new_positions, manifold, splitted = tick(manifold, current_pos, height, width)

    if splitted:
        left_timelines = 0
        right_timelines = 0

        if new_positions[0] not in cheat_sheet:
            cheat_sheet[new_positions[0]] = get_timelines(manifold, new_positions[0], height, width)
            left_timelines = cheat_sheet[new_positions[0]]
        else:
            left_timelines = cheat_sheet[new_positions[0]]

        if new_positions[1] not in cheat_sheet:
            cheat_sheet[new_positions[1]] = get_timelines(manifold, new_positions[1], height, width)
            right_timelines = cheat_sheet[new_positions[1]] 
        else:
            right_timelines = cheat_sheet[new_positions[1]] 

        return left_timelines + right_timelines + 1

    return get_timelines(manifold, nex_pos, height, width)

def main():
    manifold = read_problem("input.txt")
    start_pos = find_s_pos(manifold)
    width = len(manifold[0])
    height = len(manifold)

    timelines = get_timelines(manifold, start_pos, height, width) + 1

    print("Number of timelines is {}".format(timelines))

main()