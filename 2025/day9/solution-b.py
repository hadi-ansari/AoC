from reader import read_problem
from itertools import combinations


Y_INDEX = 0
X_INDEX = 1

distances = {}

def print_grid(coordinates):
    max_x = 0
    max_y = 0

    for c in coordinates:
        if c[X_INDEX] > max_x:
            max_x = c[X_INDEX]
        if c[Y_INDEX] > max_y:
            max_y = c[Y_INDEX]
    
    grid = []
    for y in range(max_y + 1):
        line = []
        for x in range(max_x + 1):
            curr = tuple((y, x))
            if curr in coordinates:
                line.append("#")
            else:
                line.append(".")
        
        grid.append(line)

    for l in grid:
        print(l)

def calculate_area(combo):
    c1 = combo[0]
    c2 = combo[1]

    area = (abs(c1[X_INDEX] - c2[X_INDEX]) + 1) * (abs(c1[Y_INDEX] - c2[Y_INDEX]) + 1)

    return area

def main():
    max_area = 0
    coordinates = read_problem("input.txt")

    combos = combinations(coordinates, 2)

    for combo in combos:
        area = calculate_area(combo)
        if area > max_area:
            max_area = area

    print("Answer {}".format(max_area))


    

main()