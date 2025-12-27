from reader import read_problem

Y_INDEX = 0
X_INDEX = 1

SHAPES = "shapes"
REGIONS = "regions"
SIZE = "size"
PRESENTS = "presents"

def get_shape_area(shape):
    area = 0
    for l in shape:
        for c in l:
            if c == "#":
                area += 1
    return area

def solve(problem):
    shapes = problem[SHAPES]
    regions = problem[REGIONS]
    sum = 0

    for r in regions:
        area_sum = 0

        for i in range(len(r[PRESENTS])):
            shape_area = get_shape_area(shapes[i])
            count = r[PRESENTS][i]
            area_sum += count * shape_area

        
        if area_sum <= r[SIZE][Y_INDEX] *  r[SIZE][X_INDEX]:
            sum += 1

    return sum


def main():
    problem = read_problem("input.txt")

    answer = solve(problem)
    
    print("Answer {}".format(answer))

main()