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


def is_neighbour(map, y, x, y1, x1):
    if y > len(map) -1 or y < 0 or x > len(map[y]) - 1 or x < 0:
        return False
    
    if y1 > len(map) -1 or y1 < 0 or x1 > len(map[y]) - 1 or x1 < 0:
        return False
    
    if map[y][x] == map[y1][x1]:
        return True

  
    return False

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

def not_same_region(map, dir, y, x):
    if dir == "UP" and ((y >= 1 and map[y - 1][x] != map[y][x]) or y == 0):
        return True
    if dir == "RIGHT" and( (x < len(map[y]) - 1 and map[y][x + 1] != map[y][x]) or x == len(map[y]) -1):

        return True
    if dir == "DOWN" and ((y < len(map) - 1 and map[y + 1][x] != map[y][x]) or y == len(map) - 1):

        return True
    if dir == "LEFT" and ((x >= 1 and map[y][x - 1] != map[y][x]) or x == 0):

        return True
    
    return False

def calculate_area(region):
    return len(region)

def get_corners(map, pos, visited):
    sum_corners = 0
    if not_same_region(map, "UP", pos[0], pos[1]) and not_same_region(map, "LEFT", pos[0], pos[1]):
        sum_corners += 1
    if not_same_region(map, "UP", pos[0], pos[1]) and not_same_region(map, "RIGHT", pos[0], pos[1]):
        sum_corners += 1
    if not_same_region(map, "DOWN", pos[0], pos[1]) and not_same_region(map, "LEFT", pos[0], pos[1]):
        sum_corners += 1
    if not_same_region(map, "DOWN", pos[0], pos[1]) and not_same_region(map, "RIGHT", pos[0], pos[1]):
        sum_corners += 1

    # Outer corners
    # _|
    if not_same_region(map, "UP", pos[0], pos[1]) and (is_neighbour(map, pos[0], pos[1], pos[0], pos[1] + 1) and is_neighbour(map, pos[0], pos[1] + 1, pos[0] - 1, pos[1] + 1)):
        if ((pos[0], pos[1]), (pos[0] , pos[1] + 1), (pos[0] - 1, pos[1] + 1)) not in visited:
            visited.add(((pos[0], pos[1]), (pos[0] , pos[1] + 1), (pos[0] - 1, pos[1] + 1)))
            sum_corners += 1
    # |_
    if not_same_region(map, "UP", pos[0], pos[1]) and (is_neighbour(map, pos[0], pos[1], pos[0], pos[1] - 1) and is_neighbour(map, pos[0], pos[1] - 1, pos[0] - 1, pos[1] - 1)):
        visited.add(((pos[0], pos[1]), (pos[0], pos[1] - 1), (pos[0] - 1, pos[1] - 1)))

        sum_corners += 1
    #  _
    # |
    if not_same_region(map, "DOWN", pos[0], pos[1]) and (is_neighbour(map, pos[0], pos[1], pos[0], pos[1] - 1) and is_neighbour(map, pos[0], pos[1] - 1, pos[0] + 1, pos[1] - 1)):
        if ((pos[0], pos[1]), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1)) not in visited:
            visited.add(((pos[0], pos[1]), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1)))
            sum_corners += 1
    # _
    #  |
    if not_same_region(map, "DOWN", pos[0], pos[1]) and (is_neighbour(map, pos[0], pos[1], pos[0], pos[1] + 1) and is_neighbour(map, pos[0], pos[1] + 1, pos[0] + 1, pos[1] + 1)):
        if ((pos[0], pos[1]), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)) not in visited:
            visited.add(((pos[0], pos[1]), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)))
            sum_corners += 1
    
    return sum_corners, visited

def find_sides(map, region):
    sum = 0
    visited = set()
    for pos in region:
        corners, new_visited = get_corners(map, pos, visited)
        sum += corners
        visited = new_visited

    return sum

def find_region(map, y, x):
    queue = []
    queue.append((y, x))
    visited = set()
    visited.add((y,x))

    while len(queue) > 0:
        pos = queue.pop(0)
        neighbours = find_neighbours(map, pos[0], pos[1])

        for n in neighbours:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    
    sides = find_sides(map, visited)
    return visited, sides

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