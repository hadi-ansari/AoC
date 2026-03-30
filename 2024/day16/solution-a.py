from reader import read_problem
from enum import Enum

# TOP RIGHT DOWN LEFT
DIRS = Enum('DIRS', ["UP", "RIGHT", "DOWN", "LEFT"])

UP_IDX = -1
RIGHT_IDX = 1
DOWN_IDX = 1
LEFT_IDX = -1

X = 0
Y = 1

def find_neighbours(maze, pos):
    neigbours = []
    if pos[Y] >= 1 and maze[pos[Y] + UP_IDX][pos[X]] == ".":
        neigbours.append((pos[X], pos[Y] + UP_IDX))
    if pos[Y] < len(maze) - 1 and maze[pos[Y] + DOWN_IDX][pos[X]] == ".":
        neigbours.append((pos[X], pos[Y] + DOWN_IDX))
    if pos[X] < len(maze[pos[Y]]) - 1 and maze[pos[Y]][pos[X] + RIGHT_IDX] == ".":
        neigbours.append((pos[X] + RIGHT_IDX, pos[Y]))
    if pos[X] >= 1 and maze[pos[Y]][pos[X] + LEFT_IDX] == ".":
        neigbours.append((pos[X] + LEFT_IDX, pos[Y]))
    return neigbours

def get_new_dir(dir, prev, curr):
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

# Returns the cost of moving from curr to next with the current dir
def get_cost_to_next_node(curr, next, dir):
    turn_cost = 1000
    move_cost = 1
    if dir == DIRS.UP:
        if next[X] != curr[X]:
            return turn_cost + move_cost
        elif next[Y] > curr[Y]:
            return turn_cost * 2 + move_cost
        else:
            return move_cost
        
    if dir == DIRS.DOWN:
        if next[X] != curr[X]:
            return turn_cost + move_cost
        elif next[Y] < curr[Y]:
            return turn_cost * 2 + move_cost
        else:
            return move_cost
    
    if dir == DIRS.RIGHT:
        if next[Y] != curr[Y]:
            return turn_cost + move_cost
        elif next[X] < curr[X]:
            return turn_cost * 2 + move_cost
        else:
            return move_cost
        
    if dir == DIRS.LEFT:
        if next[Y] != curr[Y]:
            return turn_cost + move_cost
        elif next[X] > curr[X]:
            return turn_cost * 2 + move_cost
        else:
            return move_cost


def get_path_and_cost(maze, start, end, initial_dir):
    visited = []
    queue = []
    neighbours = []
    path = {}
    pos = start
    prev = None
    dir = initial_dir

    # (pos, prev, heuristic, dir, prev_dir)
    queue.append((pos, prev, 0, dir, None))
    current_cost = 0

    while len(queue) > 0:
        new_node = queue.pop(0)
        pos = new_node[0]
        prev = new_node[1]
        current_cost = new_node[2]
        dir = new_node[3]
        prev_dir = new_node[4]

        if (pos, dir) in visited:
            continue
        visited.append((pos, dir))
    
        path[(pos, dir)] = (prev, prev_dir)
        if pos == end:
            temp = (end, dir)
            final_path = []
            while True:
                final_path.append(temp[0])
                prev_pos, prev_dir = path[temp]
                if prev_pos == start:
                    final_path.append(start)
                    final_path.reverse()
                    return final_path, current_cost
                temp = (prev_pos, prev_dir)

        neighbours = find_neighbours(maze, pos)
        for n in neighbours:
            new_dir = get_new_dir(dir, pos, n)
            if (n, new_dir) not in visited:
                cost_to_n = get_cost_to_next_node(pos, n, dir)
                queue.append((n, pos, cost_to_n + current_cost, new_dir, dir))
                queue = sorted(queue, key=lambda x: x[2])

        prev = pos

    return True


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
    final_path, cost = get_path_and_cost(maze, start, end, initial_dir)

    draw_maze_with_path(maze, final_path)

    print("Lowest score => ", cost)

main()