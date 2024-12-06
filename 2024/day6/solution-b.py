from reader import read_problem
import copy

def find_start(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "^" or map[y][x]  == "<" or map[y][x]  == ">" or map[y][x]  == "v":
                print("found gaurd at pos y: {}, x: {}".format(y, x))
                return (y, x)
    return False

def print_map(map):
    for l in map:
        print(l)
    print()


def turn_right(map, pos):
    if map[pos[0]][pos[1]] == "^":
        map[pos[0]][pos[1]] = ">"
    elif map[pos[0]][pos[1]]  == ">":
        map[pos[0]][pos[1]] = "v"
    elif map[pos[0]][pos[1]] == "v":
        map[pos[0]][pos[1]] = "<"
    else:
        map[pos[0]][pos[1]] = "^"

def move_forward(map, pos):
    gaurd = map[pos[0]][pos[1]] 
    if map[pos[0]][pos[1]] == "^":
        map[pos[0] - 1][pos[1]] = gaurd
        map[pos[0]][pos[1]] = "."
        return (pos[0] - 1, pos[1])
    
    elif map[pos[0]][pos[1]] == ">":
        map[pos[0]][pos[1] + 1] = gaurd
        map[pos[0]][pos[1]] = "."
        return (pos[0], pos[1] + 1)

    elif map[pos[0]][pos[1]] == "v":
        map[pos[0] + 1][pos[1]] = gaurd
        map[pos[0]][pos[1]] = "."
        return (pos[0] + 1, pos[1])

    else:
        map[pos[0]][pos[1] - 1] = gaurd
        map[pos[0]][pos[1]] = "."
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
        
def act(map, pos, next):
    if next == "#" or next == "O":
        turn_right(map, pos)
        return pos
    else:
        return move_forward(map, pos)

def has_loop(pos, dir, visited):
    for v in visited:
        if v[1] == dir and v[0] == pos:
            return True

    return False

def tick(map, pos, visited):
      dir = None

      if map[pos[0]][pos[1]] == "^":
        dir = "UP"
      elif map[pos[0]][pos[1]]  == ">":
        dir = "RIGHT"
      elif map[pos[0]][pos[1]] == "v":
          dir = "DOWN"
      else:
        dir = "LEFT"
    
      if has_loop(pos, dir, visited):
          return True, pos

      visited.add((pos, dir))
      
    
      next = find_next(map, pos, dir)

      if next:
          new_pos = act(map, pos, next)
          return False, new_pos
      else:
          return False, False
          

def main():
    map = read_problem("input.txt")

    initial_pos = find_start(map)
    loop_counter = 0


    visited = set()

    pos = initial_pos
    new_map = copy.deepcopy(map)


    while True:
        loop, pos = tick(new_map, pos, visited)
        if not pos:
            break

    final = set()
    for v in visited:
        final.add(v[0])

    counter = 0
    for y, x in final:
        counter += 1
        if initial_pos[0] == y and initial_pos[1] == y:
            continue
        new_map = copy.deepcopy(map)
        new_map[y][x] = "O"
        visited = set()

        pos = initial_pos

        while True:
            loop, pos = tick(new_map, pos, visited)
            if loop:
                loop_counter += 1
                break
            if not pos:
                break

    print("sum => ", loop_counter)


main()