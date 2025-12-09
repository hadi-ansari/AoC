from reader import read_problem
from itertools import combinations

Y_INDEX = 0
X_INDEX = 1

vertical_sides = {}
horizontal_sides = {}

def is_vertical_adjacent(c1, c2):
    return c1[X_INDEX] == c2[X_INDEX]

def is_horizontal_adjacent(c1, c2):
    return c1[Y_INDEX] == c2[Y_INDEX]

def get_all_sides(coordinates):
    combos = combinations(coordinates, 2)

    for c in combos:
        if is_vertical_adjacent(c[0], c[1]):
            vertical_sides[c[0][X_INDEX]] = (min(c[0][Y_INDEX], c[1][Y_INDEX]), max(c[0][Y_INDEX], c[1][Y_INDEX])) 
        elif is_horizontal_adjacent(c[0], c[1]):
            horizontal_sides[c[0][Y_INDEX]] = (min(c[0][X_INDEX], c[1][X_INDEX]), max(c[0][X_INDEX], c[1][X_INDEX]))

           
def calculate_area(combo):
    c1 = combo[0]
    c2 = combo[1]

    return (abs(c1[X_INDEX] - c2[X_INDEX]) + 1) * (abs(c1[Y_INDEX] - c2[Y_INDEX]) + 1)

def find_sides(c1, c2):
    min_y = min(c1[Y_INDEX], c2[Y_INDEX])
    max_y = max(c1[Y_INDEX], c2[Y_INDEX])

    min_x = min(c1[X_INDEX], c2[X_INDEX])
    max_x = max(c1[X_INDEX], c2[X_INDEX])

    top_horizontal_side = (min_y, (min_x, max_x))
    right_vertical_side = (max_x, (min_y, max_y))
    bottom_horizontal_side = (max_y, (min_x, max_x))
    left_vertical_side = (min_x, (min_y, max_y))

    return top_horizontal_side, right_vertical_side, bottom_horizontal_side, left_vertical_side

def is_vertically_inside_right(side):
    x = side[0]

    relevant_sides = []

    for key in vertical_sides:
        if key >= x:
            relevant_sides.append(vertical_sides[key])

    y_start = side[1][0]
    y_end = side[1][1]

    for r in relevant_sides:
        if r[0] <= y_start and r[1] >= y_end:
            return True
        elif r[0] >= y_start and r[1] < y_end:
            y_start = r[1]
        elif r[0] > y_start and r[1] >= y_end:
            y_end = r[0]

        if y_start >= y_end:
            return True

    return False

def is_vertically_inside_left(side):
    x = side[0]

    relevant_sides = []
    for key in vertical_sides:
        if key <= x:
            relevant_sides.append(vertical_sides[key])
 
    y_start = side[1][0]
    y_end = side[1][1]

    for r in relevant_sides:
        if r[0] <= y_start and r[1] >= y_end:
            return True
        elif r[0] >= y_start and r[1] < y_end:
            y_start = r[1]
        elif r[0] > y_start and r[1] >= y_end:
            y_end = r[0]

        if y_start >= y_end:
            return True

    return False


def is_horizontally_inside_top(side):
    y = side[0]

    relevant_sides = []
    for key in horizontal_sides:
        if key <= y:
            relevant_sides.append(horizontal_sides[key])

    x_start = side[1][0]
    x_end = side[1][1]

    for r in relevant_sides:
        if r[0] <= x_start and r[1] >= x_end:
            return True
        elif r[0] >= x_start and r[1] < x_end:
            x_start = r[1]
        elif r[0] > x_start and r[1] >= x_end:
            x_end = r[0]

        if x_start >= x_end:
            return True
    
    return False

def is_horizontally_inside_bottom(side):
    y = side[0]

    relevant_sides = []
    for key in horizontal_sides:
        if key >= y:
            relevant_sides.append(horizontal_sides[key])
    
    x_start = side[1][0]
    x_end = side[1][1]

    for r in relevant_sides:
        if r[0] <= x_start and r[1] >= x_end:
            return True
        elif r[0] >= x_start and r[1] < x_end:
            x_start = r[1]
        elif r[0] > x_start and r[1] >= x_end:
            x_end = r[0]

        if x_start >= x_end:
            return True
    
    return False


def main():
    max_area = 0
    coordinates = read_problem("input.txt")
    
    get_all_sides(coordinates)

    combos = combinations(coordinates, 2)

    for combo in combos:
        c1 = combo[0]
        c2 = combo[1]
        t, r, b, l = find_sides(c1, c2)

        if is_horizontally_inside_top(t) and is_horizontally_inside_bottom(b) and is_vertically_inside_right(r) and is_vertically_inside_left(l):
            area = calculate_area(combo)
            if area > max_area:
                max_area = area
            
    print("Answer {}".format(max_area))

main()