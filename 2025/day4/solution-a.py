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
    grid = read_problem("input.txt")
    sum = 0


    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@" and is_accessible(grid, x, y):
                sum += 1



    print("Count:", sum)


main()