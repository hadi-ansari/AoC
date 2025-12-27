from reader import read_problem
import copy
import functools

VERBOSE = False

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

def get_region_with_shape(shape, size):
    shape_w = 0
    shape_h = 0

    for y in range(len(shape)):
        for x in range(len(shape)):
            if shape[y][x] == "#" and y + 1 > shape_h:
                shape_h = y + 1
            if shape[y][x] == "#" and x + 1 > shape_h:
                shape_w = x + 1


    if VERBOSE:
        print("width {} and height {}".format(shape_w, shape_h))
        for l in shape:
            print(l)
        print()

    coordinates = []
    for y in range(size[Y_INDEX]):
        for x in range(size[X_INDEX]):
           if size[Y_INDEX] - y >= shape_h and size[X_INDEX] - x >= shape_w:
               coordinates.append((y, x))

    regions = []

    
    for p in coordinates:
        shape_in_region_coordinates = []
        for y in range(len(shape)):
            for x in range(len(shape)):
                if shape[y][x] == "#":
                    shape_in_region_coordinates.append((y + p[Y_INDEX],x + p[X_INDEX]))

        region = [["." for x in range(size[X_INDEX])] for y in range(size[Y_INDEX])]
        for y in range(size[Y_INDEX]):
            for x in range(size[X_INDEX]):
                if (y, x) in shape_in_region_coordinates:
                   region[y][x] = "#"
        regions.append(region)

        if VERBOSE:
            print("Region after placing shape in {} is:".format(p))
            for l in region:
                print(l)
            print()
    
    return regions


def main():
    sum = 0
    problem = read_problem("input-example-1.txt")

    # draw_problem(problem)
    presents_all_combos = []
    region_states = []

    for idx in range(len(problem[SHAPES])):
        p = problem[SHAPES][idx]
        if VERBOSE:
            print("initial")
            for l in p:
                print(l)
            print()
      
        all_possible_shapes = [p]
        for present_idx in range(1, 4):
            temp_r = rotate_right(p, present_idx)
            if temp_r not in all_possible_shapes:
                all_possible_shapes.append(temp_r)
        fv = flipp_present_vertically(p)
        fh = flipp_present_horizontally(p)
        if fv not in all_possible_shapes:
            all_possible_shapes.append(fv)
        # else:
        #     print("Flipped horisontally already exists")

        if fh not in all_possible_shapes:
            all_possible_shapes.append(fh)
        # else:
        #     print("Flipped vertically already exists")
        
        print("All possible shapes index {} is {}".format(idx, len(all_possible_shapes)))
        presents_all_combos.append(all_possible_shapes)

    all_regions = []
    for i in range(len(presents_all_combos)):
        present_combo = presents_all_combos[i]
        print("=" * 50)
        print("Shape index {}".format(i))
        print()
        present_region = []
        for shape in present_combo:
            present_region += get_region_with_shape(shape, problem[REGIONS][0][SIZE])

        print("It generated {} different region states".format(len(present_region)))
        all_regions.append(present_region)

    return
    for region in problem[REGIONS]:
        for present_idx in range(len(region[PRESENTS])):
            present_count = region[PRESENTS][present_idx]
            print("{}".format(present_count))
            ## TODO: solve the problem
            # for present_shapres in presents_all_combos:
            #     for shape in present_shapres:
            #         coordinates = []
            #         find_coordinates(shape, region[SIZE])
            #         return
        break


    # TBD
    print("Answer {}".format(sum))
    
main()