from reader import read_problem

def solve(claw_machine):
    a_x = claw_machine[0][0]
    a_y = claw_machine[0][1]

    b_x = claw_machine[1][0]
    b_y = claw_machine[1][1]

    p_x = claw_machine[2][0]
    p_y = claw_machine[2][1]
    
    a_total = 0
    b_total = 0

    if ((b_y * p_x) - (b_x * p_y)) % ((a_x * b_y) - (b_x * a_y)) == 0:
        a_total = ((b_y * p_x) - (b_x * p_y)) // ((a_x * b_y) - (b_x * a_y))
    if ((p_x * a_y) - (p_y * a_x)) % ((b_x * a_y) - (a_x * b_y)) == 0:
        b_total = ((p_x * a_y) - (p_y * a_x)) // ((b_x * a_y) - (a_x * b_y))

    return a_total * 3 + b_total

def main():
    claw_machines = read_problem("input.txt")
    sum = 0

    for c in claw_machines:
        sum += solve(c)

    
    print("sum is => ", sum)

main()