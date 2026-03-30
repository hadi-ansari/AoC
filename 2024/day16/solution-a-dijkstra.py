from reader import read_problem
from enum import Enum
import heapq

DIRS = Enum('DIRS', ["UP", "RIGHT", "DOWN", "LEFT"])

X = 0
Y = 1

# direction -> (dx, dy)
DIR_DELTA = {
    DIRS.UP: (0, -1),
    DIRS.DOWN: (0, 1),
    DIRS.RIGHT: (1, 0),
    DIRS.LEFT: (-1, 0),
}

def turn_left(d):
    order = [DIRS.UP, DIRS.LEFT, DIRS.DOWN, DIRS.RIGHT]
    return order[(order.index(d) + 1) % 4]

def turn_right(d):
    order = [DIRS.UP, DIRS.RIGHT, DIRS.DOWN, DIRS.LEFT]
    return order[(order.index(d) + 1) % 4]


def dijkstra(maze, start, end, initial_dir):
    # state: (cost, tiebreaker, x, y, dir)
    heap = []
    counter = 0
    heapq.heappush(heap, (0, counter, start[X], start[Y], initial_dir))
    dist = {}
    dist[(start[X], start[Y], initial_dir)] = 0
    came_from = {}
    came_from[(start[X], start[Y], initial_dir)] = None

    while heap:
        cost, _, cx, cy, cdir = heapq.heappop(heap)

        if (cx, cy) == end:
            # reconstruct path
            path = []
            state = (cx, cy, cdir)
            while state is not None:
                path.append((state[0], state[1]))
                state = came_from[state]
            path.reverse()
            return path, cost

        if cost > dist.get((cx, cy, cdir), float('inf')):
            continue

        # Option 1: move forward
        dx, dy = DIR_DELTA[cdir]
        nx, ny = cx + dx, cy + dy
        if 0 <= ny < len(maze) and 0 <= nx < len(maze[ny]) and maze[ny][nx] == ".":
            new_cost = cost + 1
            state = (nx, ny, cdir)
            if new_cost < dist.get(state, float('inf')):
                dist[state] = new_cost
                came_from[state] = (cx, cy, cdir)
                counter += 1
                heapq.heappush(heap, (new_cost, counter, nx, ny, cdir))

        # Option 2: turn left or right (costs 1000, no movement)
        for new_dir in [turn_left(cdir), turn_right(cdir)]:
            new_cost = cost + 1000
            state = (cx, cy, new_dir)
            if new_cost < dist.get(state, float('inf')):
                dist[state] = new_cost
                came_from[state] = (cx, cy, cdir)
                counter += 1
                heapq.heappush(heap, (new_cost, counter, cx, cy, new_dir))

    return None, float('inf')


def draw_maze_with_path(maze, path):
    path_set = set(path)
    for y in range(len(maze)):
        line = ""
        for x in range(len(maze[y])):
            if (x, y) in path_set:
                line += "+"
            elif maze[y][x] == ".":
                line += " "
            else:
                line += maze[y][x]
        print(line)

    print()

def main():
    maze, start, end = read_problem("input.txt")
    initial_dir = DIRS.RIGHT
    final_path, cost = dijkstra(maze, start, end, initial_dir)

    print("Final path => ", final_path)

    draw_maze_with_path(maze, final_path)

    print("Lowest score => ", cost)

main()