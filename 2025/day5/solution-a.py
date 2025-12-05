from reader import read_problem

def is_fresh(item, ranges):
    for r in ranges:
        if item in r:
            return True
        
    return False

def main():
    ranges, items = read_problem("input.txt")
    sum = 0
    
    for item in items:
        if is_fresh(item, ranges):
            sum += 1

    print("Sum of fresh items:", sum)

main()