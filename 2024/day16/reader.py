X = 0
Y = 1

def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()
    maze = []

    for l in lines:
        maze.append(list("".join(l.strip())))

    start = (-1, -1)
    end = (-1, -1)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "S":
                start = (x, y)
                maze[y][x] = "."
            elif maze[y][x] == "E":
                end = (x, y)
                maze[y][x] = "."


    input_file.close()

    return maze, start, end
