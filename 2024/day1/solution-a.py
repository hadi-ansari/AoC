from reader import read_problem

def main():
    first_col, second_col = read_problem("input.txt")
    first_col.sort()
    second_col.sort()
    total_distance = 0
    while len(first_col) > 0:
        first_min = first_col.pop()
        second_min = second_col.pop()
        total_distance += abs(int(first_min) - int(second_min))

    print("Total distance => {}".format(total_distance))
    
        

main()