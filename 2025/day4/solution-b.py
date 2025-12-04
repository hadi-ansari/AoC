from reader import read_problem

def is_accessible(grid, x, y):
    adjacent_paper_counter = 0

    if x > 0:
        if grid[y][x-1] == "@":
            adjacent_paper_counter += 1
        if y > 0 and grid[y-1][x-1] == "@":
            adjacent_paper_counter += 1
        if y < len(grid) - 1 and grid[y+1][x-1] == "@":
            adjacent_paper_counter += 1
    


    if x < len(grid[y]) - 1:
        if grid[y][x+1] == "@":
            adjacent_paper_counter += 1
        if y > 0 and grid[y-1][x+1] == "@":
            adjacent_paper_counter += 1
        if y < len(grid) - 1 and grid[y+1][x+1] == "@":
            adjacent_paper_counter += 1
    
    if y > 0 and grid[y-1][x] == "@":
        adjacent_paper_counter += 1
    if y < len(grid) - 1 and grid[y+1][x] == "@":
        adjacent_paper_counter += 1


    return adjacent_paper_counter < 4


def main():
    str_grid = read_problem("input.txt")

    grid = []

    for l in str_grid:
        grid.append(list(l))

    sum = 0


    temp_sum = -1
    while temp_sum != 0:
        temp_sum = 0
        remove_papers_pos = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "@" and is_accessible(grid, x, y):
                    remove_papers_pos.append((x, y))
                    temp_sum += 1

        for pos in remove_papers_pos:
            grid[pos[1]][pos[0]] = "."
        sum += temp_sum


    print("Count:", sum)


main()