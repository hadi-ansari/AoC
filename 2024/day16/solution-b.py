from reader import read_problem
from enum import Enum
from heapq import heapify, heappop, heappush

# TOP RIGHT DOWN LEFT
DIRS = Enum('DIRS', ["UP", "RIGHT", "DOWN", "LEFT"])

UP_IDX = -1
RIGHT_IDX = 1
DOWN_IDX = 1
LEFT_IDX = -1

X = 0
Y = 1

INFINITE = 999999

def find_neighbours(maze, pos):
    neigbours = []
    if pos[Y] < len(maze) - 1 and maze[pos[Y] + UP_IDX][pos[X]] == ".":
        neigbours.append((pos[X], pos[Y] + UP_IDX))
    if pos[Y] >= 1 and maze[pos[Y] + DOWN_IDX][pos[X]] == ".":
        neigbours.append((pos[X], pos[Y] + DOWN_IDX))
    if pos[X] < len(maze[pos[Y]]) + DOWN_IDX and maze[pos[Y]][pos[X] + RIGHT_IDX] == ".":
        neigbours.append((pos[X] + RIGHT_IDX, pos[Y]))
    if pos[X] >= 1 and maze[pos[Y]][pos[X] + LEFT_IDX] == ".":
        neigbours.append((pos[X] + LEFT_IDX, pos[Y]))
    return neigbours

def get_dir(dir, prev, curr):
    if dir == DIRS.UP:
        if curr[X] > prev[X]:
            return DIRS.RIGHT
        elif curr[X] < prev[X]:
            return DIRS.LEFT
        else:
            return dir
        
    if dir == DIRS.DOWN:
        if curr[X] > prev[X]:
            return DIRS.RIGHT
        elif curr[X] < prev[X]:
            return DIRS.LEFT
        else:
            return dir
    
    if dir == DIRS.RIGHT:
        if curr[Y] > prev[Y]:
            return DIRS.DOWN
        elif curr[Y] < prev[Y]:
            return DIRS.UP
        else:
            return dir
        
    if dir == DIRS.LEFT:
        if curr[Y] > prev[Y]:
            return DIRS.DOWN
        elif curr[Y] < prev[Y]:
            return DIRS.UP
        else:
            return dir

def get_distance(curr, next, dir):
    score = 1000
    if dir == DIRS.UP:
        if next[X] != curr[X]:
            return score + 1
        elif next[Y] > curr[Y]:
            return score * 2 + 1
        else:
            return 1
        
    if dir == DIRS.DOWN:
        if next[X] != curr[X]:
            return score + 1
        elif next[Y] < curr[Y]:
            return score * 2 + 1
        else:
            return 1
    
    if dir == DIRS.RIGHT:
        if next[Y] != curr[Y]:
            return score + 1
        elif next[X] < curr[X]:
            return score * 2 + 1
        else:
            return 1
        
    if dir == DIRS.LEFT:
        if next[Y] != curr[Y]:
            return score + 1
        elif next[X] > curr[X]:
            return score * 2 + 1
        else:
            return 1
        


def calculate_rotation_in_path(path, initial_dir):
    sum = 0
    curr = path[0]
    dir = initial_dir

    for i in range(1, len(path)):
        if get_distance(curr, path[i], dir) >= 1000:
            sum += 1
            dir = get_dir(dir, curr, path[i])
        curr = path[i]

    return sum
        

def draw_maze(maze, start, end):
    for y in range(len(maze)):
        line = ""
        for x in range(len(maze[y])):
            if (x, y) == start:
                line += "S"
            elif (x, y) == end:
                line += "E"
            else:
                line += maze[y][x]
        print(line)

    print()


def draw_maze_with_path(maze, path):
    for y in range(len(maze)):
        line = "{:4}".format(str(y))
        for x in range(len(maze[y])):
            if (x, y) in path:
                line += "O"
            elif maze[y][x] == ".":
                line += " "
            else:
                line += maze[y][x]
        print(line)

    print()

def update_distance(distances, prev, curr, new_distance, new_dir):
    if distances[curr][0] > new_distance:
        distances[curr] = (new_distance, prev, new_dir)

def get_min_unvisited_node(distances, visited):
    min_distance = INFINITE
    min_node = None

    for k in distances:
        if distances[k][0] < min_distance and visited[k] == False:
            min_distance = distances[k][0]
            min_node = k
    
    return min_node

def dijkstra(maze, start, end, dir):
    visited = {}
    distances = {}
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "." and (x, y) != start:
                distances[(x, y)] = (INFINITE, None, None) # distance, previous node and direction in the node
            elif (x, y) == start:
                distances[(x, y)] = (0, None, dir) # distance, previous node and direction in the node
            visited[(x, y)] = False

    while True:
        curr_node = get_min_unvisited_node(distances, visited)

        if not curr_node:
            print(distances[end][0])
            return
        
        curr_dir = distances[curr_node][2]
        curr_distance = distances[curr_node][0]

        neighbours = find_neighbours(maze, curr_node)

        for n in neighbours:
            new_dir = get_dir(curr_dir, curr_node, n)
            new_distance = get_distance(curr_node, n, curr_dir)
            update_distance(distances, curr_node, n, curr_distance + new_distance, new_dir)
        
        visited[curr_node] = True


def main():
    maze, start, end = read_problem("input.txt")

    dijkstra(maze, start, end, DIRS.RIGHT)


main()