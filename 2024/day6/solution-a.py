from reader import read_problem

def find_start(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "^" or map[y][x]  == "<" or map[y][x]  == ">" or map[y][x]  == "v":
                print("found garud at pos y: {}, x: {}".format(y, x))
                return (y, x)
    return False

def print_map(map):
    for l in map:
        print(l)


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
    if next == "#":

        turn_right(map, pos)
        return pos
    else:
        return move_forward(map, pos)


def tick(map, pos, visited):
      dir = None
      visited.append(pos)

      if map[pos[0]][pos[1]] == "^":
        dir = "UP"
      elif map[pos[0]][pos[1]]  == ">":
        dir = "RIGHT"
      elif map[pos[0]][pos[1]] == "v":
          dir = "DOWN"
      else:
        dir = "LEFT"
    
      next = find_next(map, pos, dir)
      if next:
          return act(map, pos, next)
      else:
          return False
          

def main():
    map = read_problem("input.txt")

    pos = find_start(map)
    visited = []

    while True:
        pos = tick(map, pos, visited)
        if not pos:
            break

    print("sum => ", len(set(visited)))

main()