X = 0
Y = 1

def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    robots = []
    map_x = 0
    map_y = 0

    robots = []
    for i in range(len(lines)):
        pos =(int((lines[i].strip().split("="))[1].split(",")[0]), int((lines[i].strip().split("="))[1].split(",")[1].split()[0]))
        velocity =(int((lines[i].strip().split("="))[2].split(",")[0]), int((lines[i].strip().split("="))[2].split(",")[1].split()[0]))
        if pos[X] > map_x:
            map_x = pos[X]
        if pos[Y] > map_y:
            map_y = pos[Y]
        robots.append((pos, velocity))
    
    map_x += 1
    map_y += 1

    input_file.close()

    return robots, (map_x, map_y)
