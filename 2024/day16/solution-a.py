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

def is_neighbour(maze, pos1, pos2):
    if pos1[Y] > len(maze) -1 or pos1[Y] < 0 or pos1[X] > len(maze[pos1[Y]]) - 1 or pos1[X] < 0:
        return False
    
    if pos2[Y] > len(maze) -1 or pos2[Y] < 0 or pos2[X] > len(maze[pos1[Y]]) - 1 or pos2[X] < 0:
        return False
    
    if maze[pos1[Y]][pos1[X]] == maze[pos2[Y]][pos2[X]]:
        return True
  
    return False

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

# heuristic function for a position
def heuristic(curr, next, dir):
    score = 1000
    if dir == DIRS.UP:
        if next[X] != curr[X]:
            return score
        elif next[Y] > curr[Y]:
            return score * 2
        else:
            return 1
        
    if dir == DIRS.DOWN:
        if next[X] != curr[X]:
            return score
        elif next[Y] < curr[Y]:
            return score * 2
        else:
            return 1
    
    if dir == DIRS.RIGHT:
        if next[Y] != curr[Y]:
            return score
        elif next[X] < curr[X]:
            return score * 2
        else:
            return 1
        
    if dir == DIRS.LEFT:
        if next[Y] != curr[Y]:
            return score
        elif next[X] > curr[X]:
            return score * 2
        else:
            return 1
        
def calculate_rotation_in_path(path, initial_dir):
    sum = 0
    curr = path[0]
    dir = initial_dir

    for i in range(1, len(path)):
        if heuristic(curr, path[i], dir) == 1000:
            sum += 1
            dir = get_new_dir(dir, curr, path[i])
        curr = path[i]

    return sum


# A* search
def a_start_serach(maze, start, end, initial_dir):
    visited = []
    queue = []
    neighbours = []
    path = {}
    pos = start
    prev = None
    visited.append(pos)
    dir = initial_dir
    queue.append((pos, prev, 0, dir))
    visited.append(pos)
    current_heuristic = 0

    while len(queue) > 0:
        new_node = queue.pop(0)
        pos = new_node[0]
        prev = new_node[1]
        current_heuristic = new_node[2]
        dir = new_node[3]
    
        path[pos] = prev
        if pos == end:
            temp = end
            final_path = []
            while True:
                final_path.append(temp)
                if temp in path and path[temp] == start:
                    final_path.append(start)
                    final_path.reverse()
                    return final_path
                temp = path[temp]
            break

        neighbours = find_neighbours(maze, pos)
        for n in neighbours:
            if n not in visited and n not in queue:
                h_of_n = heuristic(pos, n, dir)
                new_dir = get_new_dir(dir, pos, n)
                queue.append((n, pos, h_of_n + current_heuristic, new_dir))
                queue = sorted(queue, key=lambda x: x[2])
                visited.append(n)

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
    final_path = a_start_serach(maze, start, end, initial_dir)

    # draw_maze_with_path(maze, final_path)

    number_of_turns = calculate_rotation_in_path(final_path, initial_dir)
    print("Lowest score => ", number_of_turns * 1000 + len(final_path) - 1)

main()