from reader import read_problem

def find_neighbours(map, y, x):
    neigbours = []
    if y < len(map) - 1 and map[y + 1][x] == map[y][x]:
        neigbours.append((y + 1, x))
    if y >= 1 and map[y - 1][x] == map[y][x]:
        neigbours.append((y - 1, x))
    if x < len(map[y]) - 1 and map[y][x + 1] == map[y][x]:
        neigbours.append((y, x + 1))
    if x >= 1 and map[y][x - 1] == map[y][x]:
        neigbours.append((y, x - 1))
    return neigbours


def find_number_of_different_regions(map, y, x):
    sum = 0
    if (y < len(map) - 1 and map[y + 1][x] != map[y][x]) or y == len(map) - 1:
        sum+=1
    if (y >= 1 and map[y - 1][x] != map[y][x]) or y == 0:
        sum+=1
    if (x < len(map[y]) - 1 and map[y][x + 1] != map[y][x]) or x == len(map[y]) -1:
        sum+=1
    if (x >= 1 and map[y][x - 1] != map[y][x]) or x == 0:
        sum+=1
    return sum

def calculate_area(region):
    return len(region)

def calculate_perimeter_easy(map, region):
    sum = 0
    for i in region:
        sum += find_number_of_different_regions(map, i[0], i[1])

    return sum

def find_region(map, y, x):
    queue = []
    queue.append((y, x))
    visited = set()
    visited.add((y,x))
    permiter = 0

    while len(queue) > 0:
        pos = queue.pop(0)
        neighbours = find_neighbours(map, pos[0], pos[1])

        for n in neighbours:
            if n not in visited:
                visited.add(n)
                queue.append(n)



    permiter = calculate_perimeter_easy(map, visited)
    return visited, permiter

def main():
    map = read_problem("input.txt")
    visited = set()
    sum = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if (y, x) not in visited:
                new_visited, per = find_region(map, y, x)
                visited = visited | new_visited
                area = calculate_area(new_visited)
                sum += (per * area)

    print("sum is => ", sum)

main()