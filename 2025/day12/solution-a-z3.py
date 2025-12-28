from z3 import *
from reader import read_problem

VERBOSE = False

Y_INDEX = 0
X_INDEX = 1

SHAPES = "shapes"
REGIONS = "regions"
SIZE = "size"
PRESENTS = "presents"

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

def get_region_with_shape(shape, size):
    shape_w = 0
    shape_h = 0

    for y in range(len(shape)):
        for x in range(len(shape)):
            if shape[y][x] == "#" and y + 1 > shape_h:
                shape_h = y + 1
            if shape[y][x] == "#" and x + 1 > shape_w:
                shape_w = x + 1


    if VERBOSE:
        print("width {} and height {}".format(shape_w, shape_h))
        for l in shape:
            print(l)
        print()

    coordinates = []
    should_continue = True
    for y in range(size[Y_INDEX]):
        for x in range(size[X_INDEX]):
            if size[Y_INDEX] - y >= shape_h and size[X_INDEX] - x >= shape_w:
               coordinates.append((y, x))
            elif size[X_INDEX] - x < shape_w:
               break
            elif size[Y_INDEX] - y < shape_h:
               should_continue = False
               break
        if not should_continue:
            break


    regions = []

    
    for p in coordinates:
        region = []
        for y in range(len(shape)):
            for x in range(len(shape)):
                if shape[y][x] == "#":
                    region.append((y + p[Y_INDEX], x + p[X_INDEX]))
                    
        regions.append(region)
    
    if VERBOSE:
        for r in regions:
            draw_region(size, r)

    return regions

def draw_region(size, coordinates):
    final_region = []
    for y in range(size[Y_INDEX]):
        row = []
        for x in range(size[X_INDEX]):
            if (y, x) in coordinates:
                row.append("#")
            else:
                row.append(".")
        final_region.append(row)
    for row in final_region:
        print(row)

    print()


def solve(problem):
    shapes = problem[SHAPES]
    regions = problem[REGIONS]
    sum = 0
    variables = []

    presents_all_combos = []
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

        if fh not in all_possible_shapes:
            all_possible_shapes.append(fh)
        
        print("All possible shapes index {} is {}".format(idx, len(all_possible_shapes)))
        presents_all_combos.append(all_possible_shapes)

    all_regions = []
    
    for region_idx in range(len(problem[REGIONS])):
        sum_of_regions = 0
        region = problem[REGIONS][region_idx]
        print("*" * 60)
        print("Region idx {} ({}x{})".format(region_idx, region[SIZE][X_INDEX], region[SIZE][Y_INDEX]))
        print("*" * 60)
        curr_reg = []
        for i in range(len(presents_all_combos)):
            present_combo = presents_all_combos[i]
            # print("=" * 50)
            # print("Shape index {}".format(i))
            # print()
            present_region = []
            for shape in present_combo:
                present_region += get_region_with_shape(shape, region[SIZE])
               

            len_of_region = len(present_region)
            # print("It generated {} different region states".format(len_of_region))
            sum_of_regions += len_of_region
            curr_reg.append(present_region)
        
        all_regions.append(curr_reg)
        print("All possible placements {}".format(sum_of_regions))
        print()

    for region_idx in range(len(regions)):
        solver = Solver()
        region = regions[region_idx]
        curr_all_regions = all_regions[region_idx]

        buckets = [[[] for _ in range(region[SIZE][X_INDEX])] for _ in range(region[SIZE][Y_INDEX])]
        # region_variables = []
        # for y in range(region[SIZE][Y_INDEX]):
        #     temp = []
        #     for x in range(region[SIZE][X_INDEX]):
        #         temp.append(Int("r-" + str(y) + str(x)))
        #     region_variables.append(temp)
        condition = True
        variables = []
        for i in range(len(curr_all_regions)):
            temp_variables = []
            for j in range(len(curr_all_regions[i])):
                curr_region = curr_all_regions[i][j]
                var = Bool("bool-shape" + str(i) + "-" + "region" + str(j))
                increment = If(var, 1, 0)
                
                # if condition:
                #     print("coordinates", curr_region)
                #     print("Region for shape index {} state {}".format(i, j))
                #     draw_region(region[SIZE], curr_region)
                #     condition = False
                for c in curr_region:
                    buckets[c[Y_INDEX]][c[X_INDEX]].append(increment)
                temp_variables.append(var)

            variables.append(temp_variables)

        # Constraints
        for i in range (len(region[PRESENTS])):
            solver.add(AtMost(*variables[i], region[PRESENTS][i]))
            solver.add(AtLeast(*variables[i], region[PRESENTS][i]))

        for r in range(region[SIZE][Y_INDEX]):
            for c in range(region[SIZE][X_INDEX]):
                if buckets[r][c]:
                    cell_sum = Sum(buckets[r][c])
                    solver.add(Or(cell_sum == 1, cell_sum == 0))

        if solver.check() == sat:
            sum += 1
    return sum


def main():
    problem = read_problem("input-example-1.txt")

    answer = solve(problem)

    print("Answer {}".format(answer))

main()