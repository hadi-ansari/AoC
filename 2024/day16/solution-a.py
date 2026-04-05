from reader import read_problem
from enum import IntEnum
import heapq

# TOP RIGHT DOWN LEFT
DIRS = IntEnum('DIRS', ["UP", "RIGHT", "DOWN", "LEFT"])

UP_IDX = -1
RIGHT_IDX = 1
DOWN_IDX = 1
LEFT_IDX = -1

X_INDEX = 0
Y_INDEX = 1

INFINITE = 9999999

def find_neighbours(maze, pos):
    neigbours = []
    if pos[Y_INDEX] >= 1 and maze[pos[Y_INDEX] + UP_IDX][pos[X_INDEX]] == ".":
        neigbours.append((pos[X_INDEX], pos[Y_INDEX] + UP_IDX))
    if pos[Y_INDEX] < len(maze) - 1 and maze[pos[Y_INDEX] + DOWN_IDX][pos[X_INDEX]] == ".":
        neigbours.append((pos[X_INDEX], pos[Y_INDEX] + DOWN_IDX))
    if pos[X_INDEX] < len(maze[pos[Y_INDEX]]) - 1 and maze[pos[Y_INDEX]][pos[X_INDEX] + RIGHT_IDX] == ".":
        neigbours.append((pos[X_INDEX] + RIGHT_IDX, pos[Y_INDEX]))
    if pos[X_INDEX] >= 1 and maze[pos[Y_INDEX]][pos[X_INDEX] + LEFT_IDX] == ".":
        neigbours.append((pos[X_INDEX] + LEFT_IDX, pos[Y_INDEX]))
    return neigbours

def get_new_dir(dir, prev, curr):
    if dir == DIRS.UP:
        if curr[X_INDEX] > prev[X_INDEX]:
            return DIRS.RIGHT
        elif curr[X_INDEX] < prev[X_INDEX]:
            return DIRS.LEFT
        else:
            return dir
        
    if dir == DIRS.DOWN:
        if curr[X_INDEX] > prev[X_INDEX]:
            return DIRS.RIGHT
        elif curr[X_INDEX] < prev[X_INDEX]:
            return DIRS.LEFT
        else:
            return dir
    
    if dir == DIRS.RIGHT:
        if curr[Y_INDEX] > prev[Y_INDEX]:
            return DIRS.DOWN
        elif curr[Y_INDEX] < prev[Y_INDEX]:
            return DIRS.UP
        else:
            return dir
        
    if dir == DIRS.LEFT:
        if curr[Y_INDEX] > prev[Y_INDEX]:
            return DIRS.DOWN
        elif curr[Y_INDEX] < prev[Y_INDEX]:
            return DIRS.UP
        else:
            return dir

# Returns the distance/cost of moving from curr to next with the current dir
def get_distance_to_next_node(curr, next, dir):
    turn_cost = 1000
    move_cost = 1
    if dir == DIRS.UP:
        if next[X_INDEX] != curr[X_INDEX]:
            return turn_cost + move_cost
        elif next[Y_INDEX] > curr[Y_INDEX]:
            return turn_cost * 2 + move_cost
        else:
            return move_cost
        
    if dir == DIRS.DOWN:
        if next[X_INDEX] != curr[X_INDEX]:
            return turn_cost + move_cost
        elif next[Y_INDEX] < curr[Y_INDEX]:
            return turn_cost * 2 + move_cost
        else:
            return move_cost
    
    if dir == DIRS.RIGHT:
        if next[Y_INDEX] != curr[Y_INDEX]:
            return turn_cost + move_cost
        elif next[X_INDEX] < curr[X_INDEX]:
            return turn_cost * 2 + move_cost
        else:
            return move_cost
        
    if dir == DIRS.LEFT:
        if next[Y_INDEX] != curr[Y_INDEX]:
            return turn_cost + move_cost
        elif next[X_INDEX] > curr[X_INDEX]:
            return turn_cost * 2 + move_cost
        else:
            return move_cost

def dijkstra(maze, start, initial_dir):
    priority_q = [(0, start, initial_dir)] # (distance, pos, direction)

    distances = {}
    previous = {}
    for y in range(len(maze[0])):
        for x in range(len(maze)):
            if maze[y][x] == ".":
                for d in DIRS:
                    distances[(x,y,d)] = INFINITE
                    previous[(x,y,d)] = None
    
    distances[(start[X_INDEX], start[Y_INDEX], initial_dir)] = 0

    while len(priority_q) != 0:
        current_distance, current_node, current_dir = heapq.heappop(priority_q)

        if current_distance > distances[(current_node[X_INDEX], current_node[Y_INDEX], current_dir)]:
            continue

        for n in find_neighbours(maze, current_node):
            distance_to_next = get_distance_to_next_node(current_node, n, current_dir)
            new_dir = get_new_dir(current_dir, current_node, n)
            new_distance = current_distance + distance_to_next

            if new_distance < distances[(n[X_INDEX], n[Y_INDEX], new_dir)]:
                distances[(n[X_INDEX], n[Y_INDEX], new_dir)] = new_distance
                previous[(n[X_INDEX], n[Y_INDEX], new_dir)] = (current_node, current_dir)
                heapq.heappush(priority_q, (new_distance, n, new_dir))

    return distances, previous

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
        line = ""
        for x in range(len(maze[y])):
            if (x, y) in path:
                line += "0"
            elif maze[y][x] == ".":
                line += "."
            else:
                line += maze[y][x]
        print(line)

    print()

def get_path(previous, start, best_end_state):
    path = []
    current = best_end_state
    
    while current is not None:
        if isinstance(current, tuple) and len(current) == 2 and isinstance(current[0], tuple):
            node, direction = current
            path.append(node)
            current = previous.get((node[0], node[1], direction))
        else:
            path.append(current)
            break
    
    path.reverse()
    
    if path[0] == start:
        return path
    return []  # No path found

def main():
    maze, start, end = read_problem("input.txt")
    initial_dir = DIRS.RIGHT
    distances, previous = dijkstra(maze, start, initial_dir)


    # Find the best direction to arrive at end
    best_cost = INFINITE
    best_dir = None
    for d in DIRS:
        key = (end[0], end[1], d)
        if key in distances and distances[key] < best_cost:
            best_cost = distances[key]
            best_dir = d

    best_end_state = (end, best_dir)
    final_path = get_path(previous, start, best_end_state)

    # draw_maze_with_path(maze, final_path)

    print("Path from S to E => ", final_path)
    print("Cost of S to E => ", best_cost)

main()