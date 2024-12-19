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

INFINITE = 9999999

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

# Returns the new dir after moving from curr to next
def get_new_dir(curr, next, curr_dir):
    if curr_dir == DIRS.UP:
        if next[X] > curr[X]:
            return DIRS.RIGHT
        elif next[X] < curr[X]:
            return DIRS.LEFT
        else:
            return curr_dir
        
    if curr_dir == DIRS.DOWN:
        if next[X] > curr[X]:
            return DIRS.RIGHT
        elif next[X] < curr[X]:
            return DIRS.LEFT
        else:
            return curr_dir
    
    if curr_dir == DIRS.RIGHT:
        if next[Y] > curr[Y]:
            return DIRS.DOWN
        elif next[Y] < curr[Y]:
            return DIRS.UP
        else:
            return curr_dir
        
    if curr_dir == DIRS.LEFT:
        if next[Y] > curr[Y]:
            return DIRS.DOWN
        elif next[Y] < curr[Y]:
            return DIRS.UP
        else:
            return curr_dir

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

def draw_maze(maze, start, end):
    for y in range(len(maze)):
        line = "{:3} ".format(y)
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
        if distances[curr][0] >= new_distance:
            prev_nodes =  distances[curr][1]
            prev_nodes.append(prev)
            distances[curr] = (new_distance, prev_nodes, new_dir)

def get_min_unvisited_node(distances, visited):
    min_distance = INFINITE
    min_node = None

    for k in distances:
        if distances[k][0] < min_distance and visited[k] == False:
            min_distance = distances[k][0]
            min_node = k
    
    return min_node

def find_path_to_start(distances, curr, start, final_path):
    prev_nodes = distances[curr][1]

    for p in prev_nodes:
        if p not in final_path:
            final_path.add(p)
            if p == start:
                return final_path

            final_path = final_path | find_path_to_start(distances, p, start, final_path)

    return final_path

def get_prev_neighbour_in_same_dir(maze, curr, dir):
    if dir == DIRS.UP:
        if curr[Y] > 0 and maze[curr[Y] + DOWN_IDX][curr[X]] == ".":
            return (curr[X], curr[Y] + DOWN_IDX)
    if dir == DIRS.RIGHT:
         if curr[X] > 0 and maze[curr[Y]][curr[X] + LEFT_IDX] == ".":
            return (curr[X] + LEFT_IDX, curr[Y])
    if dir == DIRS.DOWN:
        if curr[Y] < len(maze) - 1 and maze[curr[Y] + UP_IDX][curr[X]] == ".":
            return (curr[X], curr[Y] + UP_IDX)
    if dir == DIRS.LEFT:
         if curr[X] < len(maze[0]) - 1 and maze[curr[Y]][curr[X] + RIGHT_IDX] == ".":
            return (curr[X] + RIGHT_IDX, curr[Y])
    return None

def get_next_neighbour_in_same_dir(maze, curr, dir):
    if dir == DIRS.DOWN:
        if curr[Y] > 0 and maze[curr[Y] + DOWN_IDX][curr[X]] == ".":
            return (curr[X], curr[Y] + DOWN_IDX)
    if dir == DIRS.LEFT:
         if curr[X] > 0 and maze[curr[Y]][curr[X] + LEFT_IDX] == ".":
            return (curr[X] + LEFT_IDX, curr[Y])
    if dir == DIRS.UP:
        if curr[Y] < len(maze) - 1 and maze[curr[Y] + UP_IDX][curr[X]] == ".":
            return (curr[X], curr[Y] + UP_IDX)
    if dir == DIRS.RIGHT:
         if curr[X] < len(maze[0]) - 1 and maze[curr[Y]][curr[X] + RIGHT_IDX] == ".":
            return (curr[X] + RIGHT_IDX, curr[Y])
    return None

# Adjusted dijkastra
def dijkstra(maze, start, end, dir):
    visited = {}
    distances = {}
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "." and (x, y) != start:
                distances[(x, y)] = (INFINITE, [], None) # distance, previous node and direction in the node
            elif (x, y) == start:
                distances[(x, y)] = (0, [], dir) # distance, previous node and direction in the node
            visited[(x, y)] = False

    while True:
        curr_node = get_min_unvisited_node(distances, visited)

        if not curr_node:
            final_path = set()
            final_path.add(end)
            final_path = find_path_to_start(distances, end, start, final_path)
            print("sum => ", len(final_path))
            # draw_maze_with_path(maze, final_path)
            break
        
        curr_dir = distances[curr_node][2]
        curr_distance = distances[curr_node][0]

        neighbours = find_neighbours(maze, curr_node)

        for n in neighbours:
            neighbour_dir = get_new_dir(curr_node, n, curr_dir)
            neighbour_distance = get_distance(curr_node, n, curr_dir)


            # This is because we want to find more nodes which might 
            # lead to the same cost.
            prev_neighbour_in_same_dir = get_prev_neighbour_in_same_dir(maze, curr_node, neighbour_dir)
           
            if prev_neighbour_in_same_dir and distances[prev_neighbour_in_same_dir][2]:
                prev_neighbour_to_curr_distance = get_distance(prev_neighbour_in_same_dir, curr_node, distances[prev_neighbour_in_same_dir][2])
                
                if curr_distance + neighbour_distance == distances[prev_neighbour_in_same_dir][0] + prev_neighbour_to_curr_distance + 1:
                    distances[curr_node][1].append(prev_neighbour_in_same_dir)

            next_neighbour_in_same_dir = get_next_neighbour_in_same_dir(maze, n, neighbour_dir)
            if next_neighbour_in_same_dir and distances[next_neighbour_in_same_dir][2]:
                next_neighbour_to_curr_distance = get_distance(n, next_neighbour_in_same_dir, distances[next_neighbour_in_same_dir][2])

                if distances[next_neighbour_in_same_dir][0] == distances[curr_node][0] + next_neighbour_to_curr_distance + 1:
                    distances[n][1].append(curr_node)

            update_distance(distances, curr_node, n, curr_distance + neighbour_distance, neighbour_dir)

        visited[curr_node] = True


def main():
    maze, start, end = read_problem("input.txt")

    dijkstra(maze, start, end, DIRS.RIGHT)

main()