from reader import read_problem
import copy
import functools

VERBOSE = True

Y_INDEX = 0
X_INDEX = 1

SHAPES = "shapes"
REGIONS = "regions"
SIZE = "size"
PRESENTS = "presents"

def draw_problem(problem):
    print("Presents shapes")
    for i in range(len(problem[SHAPES])):
        shape = problem[SHAPES][i]
        print("{}:".format(i))
        for l in shape:
            print(l)

    print()
    print("Regions")
    for j in range(len(problem[REGIONS])):
        region = problem[REGIONS][j]

        print("Region with size of {} x {}".format(region[SIZE][X_INDEX], region[SIZE][Y_INDEX]))
        print("Has these presents {}".format(region[PRESENTS]))

def flipp_present_horizontally(present):
    flipped_present = []

    for i in range(len(present)): 
        row = copy.deepcopy(present[i])
        row.reverse()
        flipped_present.append(row)

    if VERBOSE:
        print("Flipped horizontally")
        for l in flipped_present:
            print(l)
        print()

    
    return flipped_present


def flipp_present_vertically(present):
    flipped_present = []

    for y in range(len(present) - 1, -1, -1):
        flipped_present.append(copy.deepcopy(present[y]))

    if VERBOSE:
        print("Flipped vertically")
        for l in flipped_present:
            print(l)
        print()
    
    return flipped_present

def rotate_right(present, repeat = 1):
    rotated = copy.deepcopy(present)

    for i in range(repeat):
        temp = copy.deepcopy(rotated)
        for y in range(len(temp)):
            y_counter = 0
            temp_x = len(temp) - y - 1
            for x in range(len(temp)):
               rotated[y_counter][temp_x]= temp[y][x]
               y_counter += 1
                
    if VERBOSE:
        print("Rotated to right {} time(s)".format(repeat))
        for l in rotated:
            print(l)
        print()
    
    return rotated


def is_equal(p1, p2):
    for y in range(len(p1)):
        for x in range(len(p1)):
            if p1[y][x] != p2[y][x]:
                return False
            
    return True

def find_coordinates(shape, size):
    print(size)
    for y in range(size[Y_INDEX]):
        temp = ""
        for x in range(size[X_INDEX]):
            temp += "."
        print(temp)


def main():
    sum = 0
    problem = read_problem("input-example-1.txt")

    # draw_problem(problem)
    presents_all_combos = []

    for p in problem[SHAPES]:
        print("initial")
        for l in p:
            print(l)
        print()
      
        all_possible_shapes = [p]
        for i in range(1, 4):
            temp_r = rotate_right(p, i)
            if temp_r not in all_possible_shapes:
                all_possible_shapes.append(temp_r)
        fv = flipp_present_vertically(p)
        fh = flipp_present_horizontally(p)
        if fv not in all_possible_shapes:
            all_possible_shapes.append(fv)
        else:
            print("Flipped horisontally already exists")

        if fh not in all_possible_shapes:
            all_possible_shapes.append(fh)
        else:
            print("Flipped vertically already exists")
        
        print("all possible shapes {}".format(len(all_possible_shapes)))
        presents_all_combos.append(all_possible_shapes)
    for region in problem[REGIONS]:
        for presen_shapres in presents_all_combos:
            for shape in presen_shapres:
                coordinates = []
                find_coordinates(shape, region[SIZE])
                return


    # TBD
    print("Answer {}".format(sum))
    
main()