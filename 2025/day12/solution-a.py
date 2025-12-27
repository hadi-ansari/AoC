from reader import read_problem
import copy
import itertools

VERBOSE = False

Y_INDEX = 0
X_INDEX = 1

SHAPES = "shapes"
REGIONS = "regions"
SIZE = "size"
PRESENTS = "presents"

cheat_sheet = {}

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

def all_fits(region, all_combos):
    result = []

    for combo in all_combos:
        temp = copy.deepcopy(region)
        has_not_common_element = True
        for r in combo:
            if not set(temp).isdisjoint(r):
                has_not_common_element = False
                break
            else:
                temp += r
        
        if has_not_common_element:
            combo_coordinates = []
            for c in combo:
                combo_coordinates += c
            combo_coordinates += region
            result.append(combo_coordinates)

    return result

def does_intersect(r1, r2):
    return not set(r1).isdisjoint(r2)

def main():
    sum = 0
    problem = read_problem("input-example-1.txt")

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
        # else:
        #     print("Flipped horisontally already exists")

        if fh not in all_possible_shapes:
            all_possible_shapes.append(fh)
        # else:
        #     print("Flipped vertically already exists")
        
        print("All possible shapes index {} is {}".format(idx, len(all_possible_shapes)))
        presents_all_combos.append(all_possible_shapes)

    all_regions = []
    
    for region_idx in range(len(problem[REGIONS])):
        does_fit = True
        sum_of_regions = 0
        region = problem[REGIONS][region_idx]
        print("*" * 60)
        print("Region idx {} ({}x{})".format(region_idx, region[SIZE][X_INDEX], region[SIZE][Y_INDEX]))
        print("*" * 60)
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
            all_regions.append(present_region)
        
        print()
        print("all possible region states {}".format(sum_of_regions))
        temp_region = []
        for present_idx in range(len(region[PRESENTS])):
            present_count = region[PRESENTS][present_idx]
            relevant_region = all_regions[present_idx]
            
            print("Number of presents {} of present index {}".format(present_count, present_idx))
            print("All possible region states for this {}".format(len(relevant_region)))
            if VERBOSE:
                for r in relevant_region:
                    draw_region(region[SIZE], r)

            if present_count > 0:
                all_possible_combos = list(itertools.combinations(relevant_region, present_count))
                print(len(all_possible_combos))

                new_regions = all_fits(temp_region, all_possible_combos)
                print(len(new_regions))

                cheat_sheet[(present_count, present_idx)] = new_regions

                
        

        if does_fit:
            sum += 1

        break
    
    all_combos = []
    for key in cheat_sheet:
        p = cheat_sheet[key]
        print("len of compatible combos {} for present with index {} and number of {}".format(len(p), key[1], key[0]))
        all_combos.append(p)
        # for r in p:
        #     draw_region(region[SIZE], r)
    
    print("Total combos to check {}".format(len(all_combos)))
    lenght = 0
    for l in all_combos:
        lenght += len(l)
    
    print("len is ", lenght)

    res = list(itertools.product(*all_combos))
    print(len(res))
    condition = False
    for r in res:
        new_region = all_fits([], all_possible_combos)
        if len(new_region) > 0:
            condition = True
            break
    
    if condition:
        print("Det gick")

    

    print("Answer {}".format(sum))
    
main()