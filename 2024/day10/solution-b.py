from reader import read_problem

def find_nines(hiking_map):
    found = []
    for y in range(len(hiking_map)):
        for x in range(len(hiking_map[y])):
            if hiking_map[y][x] == 9:
                found.append((y, x))
    return found

def find_neighbours(hiking_map, y, x):
    neigbours = []
    if y < len(hiking_map) - 1 and hiking_map[y + 1][x] - hiking_map[y][x] == 1:
        neigbours.append((y + 1, x))
    if y >= 1 and hiking_map[y - 1][x] - hiking_map[y][x] == 1:
        neigbours.append((y - 1, x))
    if x < len(hiking_map[y]) - 1 and hiking_map[y][x + 1] - hiking_map[y][x] == 1:
        neigbours.append((y, x + 1))
    if x >= 1 and hiking_map[y][x - 1] - hiking_map[y][x] == 1:
        neigbours.append((y, x - 1))
    return neigbours

# DFS
def find_trailheads(hiking_map, y, x):
    total = 0
    visited = []
    queue = []
    neighbours = []
    initial = (y, x)

    queue.append(initial)
    while len(queue) > 0:
        pos = queue.pop()
        visited.append(pos)
        if hiking_map[pos[0]][pos[1]] == 9:
            total += 1
            visited = []

        neighbours = find_neighbours(hiking_map, pos[0], pos[1])
        for n in neighbours:
            if n not in visited and n not in queue:
                queue.append(n)

    return total

def main():
    hiking_map = read_problem("input.txt")
    sum = 0

    for y in range(len(hiking_map)):
        for x in range(len(hiking_map[y])):
            if hiking_map[y][x] == 0:
                sum += find_trailheads(hiking_map, y, x)

    print("sum => ", sum)


main()