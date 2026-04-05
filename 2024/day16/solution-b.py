from reader import read_problem
from enum import Enum
import heapq

# TOP RIGHT DOWN LEFT
DIRS = Enum('DIRS', ["UP", "RIGHT", "DOWN", "LEFT"])

X_INDEX = 0
Y_INDEX = 1

INFINITE = 9999999

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

def get_forward(x, y, d):
    if d == DIRS.UP:
        return x, y - 1
    elif d == DIRS.DOWN:
        return x, y + 1
    elif d == DIRS.LEFT:
        return x - 1, y
    else:  # RIGHT
        return x + 1, y

def turn_left(d):
    if d == DIRS.UP: return DIRS.LEFT
    if d == DIRS.LEFT: return DIRS.DOWN
    if d == DIRS.DOWN: return DIRS.RIGHT
    return DIRS.UP

def turn_right(d):
    if d == DIRS.UP: return DIRS.RIGHT
    if d == DIRS.RIGHT: return DIRS.DOWN
    if d == DIRS.DOWN: return DIRS.LEFT
    return DIRS.UP

def Solve(maze, start, end, initial_dir):
    # State: (x, y, direction)
    # distances maps state -> (cost, [predecessor_states])
    distances = {}
    start_state = (start[X_INDEX], start[Y_INDEX], initial_dir)
    distances[start_state] = (0, [])

    # Priority queue: (cost, x, y, dir_value)
    pq = [(0, start[X_INDEX], start[Y_INDEX], initial_dir.value)]
    visited = set()

    while pq:
        cost, x, y, dv = heapq.heappop(pq)
        d = DIRS(dv)
        state = (x, y, d)

        if state in visited:
            continue
        visited.add(state)

        # Possible transitions:
        # 1. Move forward (cost +1)
        # 2. Turn left (cost +1000)
        # 3. Turn right (cost +1000)

        transitions = []
        # Move forward
        nx, ny = get_forward(x, y, d)
        if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] == ".":
            transitions.append(((nx, ny, d), cost + 1))
        # Turn left
        transitions.append(((x, y, turn_left(d)), cost + 1000))
        # Turn right
        transitions.append(((x, y, turn_right(d)), cost + 1000))

        for new_state, new_cost in transitions:
            if new_state in visited:
                continue
            if new_state not in distances or distances[new_state][0] > new_cost:
                distances[new_state] = (new_cost, [state])
                heapq.heappush(pq, (new_cost, new_state[0], new_state[1], new_state[2].value))
            elif distances[new_state][0] == new_cost:
                distances[new_state][1].append(state)

    # Find min cost to reach end in any direction
    min_end_cost = INFINITE
    for d in DIRS:
        s = (end[X_INDEX], end[Y_INDEX], d)
        if s in distances:
            min_end_cost = min(min_end_cost, distances[s][0])

    # Backtrack from all end states with minimum cost to collect all tiles on best paths
    final_positions = set()
    queue = []
    visited_back = set()
    for d in DIRS:
        s = (end[X_INDEX], end[Y_INDEX], d)
        if s in distances and distances[s][0] == min_end_cost:
            queue.append(s)
            visited_back.add(s)

    while queue:
        state = queue.pop()
        final_positions.add((state[0], state[1]))
        for prev_state in distances[state][1]:
            if prev_state not in visited_back:
                visited_back.add(prev_state)
                queue.append(prev_state)

    print("sum => ", len(final_positions))
    draw_maze_with_path(maze, final_positions)


def main():
    maze, start, end = read_problem("input.txt")

    Solve(maze, start, end, DIRS.RIGHT)


main()