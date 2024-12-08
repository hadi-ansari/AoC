from reader import read_problem

def find_antinode(map, y, x):
    antenna = map[y][x]
    antinodes = set()
    for y_idx in range(len(map)):
        for x_idx in range(len(map[y])):
            if antenna == map[y_idx][x_idx] and y_idx != y and x_idx != x:
                anti_y = (y_idx)
                anti_x = (x_idx)
                while anti_y < len(map) and anti_y >=0 and anti_x < len(map[y]) and anti_x >= 0:
                    antinodes.add((anti_y, anti_x))
                    anti_y += (y_idx - y)
                    anti_x += (x_idx - x)

    return antinodes

def main():
    map = read_problem("input.txt")

    antinode_hash = {}

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] != ".":
                new_antinodes = find_antinode(map, y, x)
                for n in new_antinodes:
                    if map[y][x] in antinode_hash:
                        antinode_hash[map[y][x]].add(n)
                    else:
                        antinode_hash[map[y][x]] = set()
                        antinode_hash[map[y][x]].add(n)
    
    antinode_total = set()
    for k in antinode_hash:
        for v in antinode_hash[k]:
            antinode_total.add(v)

    print("sum => ", len(antinode_total))

main()