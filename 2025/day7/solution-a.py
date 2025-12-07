from reader import read_problem

Y_INDEX = 0
X_INDEX = 1

DOWN = 1
UP = -1
LEFT = -1
RIGHT = 1

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
   
    new_positions = set()


    # Last line
    if not is_in_manifold(height, width, nex_pos):
        return new_positions, manifold, False

    if manifold[nex_pos[Y_INDEX]][nex_pos[X_INDEX]] == ".":
        manifold[current_pos[Y_INDEX] + DOWN][current_pos[X_INDEX]] = "|"
        new_positions.add(nex_pos)
        return new_positions, manifold, False

    if manifold[nex_pos[Y_INDEX]][nex_pos[X_INDEX]] == "^":
        right_pos = (current_pos[Y_INDEX] + DOWN, current_pos[X_INDEX] + RIGHT)
        left_pos = (current_pos[Y_INDEX] + DOWN, current_pos[X_INDEX] + LEFT)
        if is_in_manifold(height, width, right_pos):
            manifold[right_pos[Y_INDEX]][right_pos[X_INDEX]] = "|"
            new_positions.add(right_pos)
        if is_in_manifold(height, width, left_pos):
            manifold[left_pos[Y_INDEX]][left_pos[X_INDEX]] = "|"
            new_positions.add(left_pos)
        return new_positions, manifold, True
    
    return new_positions, manifold, False



def main():
    number_of_splitting = 0
    manifold = read_problem("input.txt")

    start_pos = find_s_pos(manifold)
    width = len(manifold[0])
    height = len(manifold)
    positions = set()
    positions.add(start_pos)

    while len(positions) > 0:
        current_pos = positions.pop()
        new_positions, manifold, splitted = tick(manifold, current_pos, height, width)

        if splitted:
            number_of_splitting += 1

        positions.update(new_positions)

    print("Number of splittings is {}".format(number_of_splitting))

main()