from reader import read_problem

def find_start(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "^":
                return (y, x), "UP"
            elif map[y][x]  == ">":
                return (y, x), "RIGHT"
            elif  map[y][x]  == "v":
                return (y, x), "DOWN"
            elif map[y][x]  == "<":
                return (y, x), "LEFT"
              
    return False

def print_map(map):
    for l in map:
        print(l)
    print()


def turn_right(dir):
    if dir == "UP":
        return "RIGHT"
    if dir == "RIGHT":
       return "DOWN"
    elif dir  == "DOWN":
       return "LEFT"
    else:
        return "UP"

def move_forward(pos, dir):
    if dir == "UP":
        return (pos[0] - 1, pos[1])
    elif dir == "RIGHT":
        return (pos[0], pos[1] + 1)

    elif dir == "DOWN":
        return (pos[0] + 1, pos[1])

    else:
        return (pos[0], pos[1] - 1)


def find_next(map, pos, dir):
    if dir == "UP":
        if pos[0] <= 0:
            return False
        else:
            return map[pos[0] - 1][pos[1]]
    elif dir == "RIGHT":
        if pos[1] >= len(map[pos[0]]) - 1:
            return False
        else:
            return map[pos[0]][pos[1] + 1]
    elif dir == "DOWN":
        if pos[0] >= len(map) - 1:
            return False
        else:
            return map[pos[0] + 1][pos[1]]
    else:
        if pos[1] <= 0:
            return False
        else:
            return map[pos[0]][pos[1] - 1]
        
def act(pos, dir, next):
    if next == "#" or next == "O":
        return pos, turn_right(dir)
    else:
        return move_forward(pos, dir), dir

def has_loop(pos, dir, visited):
    if pos not in visited:
       return False
    for v in visited[pos]:
        if v == dir:
            return True

    return False

def tick(map, pos, dir, visited):
      if has_loop(pos, dir, visited):
          return True, pos, dir

      if pos not in visited:
          visited[pos] = []
          visited[pos].append(dir)
      else:
          visited[pos].append(dir)
      
      next = find_next(map, pos, dir)

      if next:
          new_pos, new_dir = act(pos, dir, next)
          return False, new_pos, new_dir
      else:
          return False, False, dir
          

def main():
    map = read_problem("input.txt")

    initial_pos, initial_dir = find_start(map)
    loop_counter = 0
    visited = {}
    pos = initial_pos
    dir = initial_dir
    map[pos[0]][pos[1]] = "."

    while True:
        loop, pos, dir = tick(map, pos, dir, visited)
        if not pos:
            break

    final = set()
    for v in visited:
        final.add(v)

    for y, x in final:
        if initial_pos[0] == y and initial_pos[1] == x:
            continue
        map[y][x] = "O"
        visited = {}
        pos = initial_pos
        dir = initial_dir

        while True:
            loop, pos, dir = tick(map, pos, dir, visited)
            if loop:
                loop_counter += 1
                break
            if not pos:
                break
        map[y][x] = "."
        

    print("sum => ", loop_counter)


main()