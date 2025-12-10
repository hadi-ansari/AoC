from reader import read_problem
from itertools import combinations

LIFHTS_INDEX = 0
BUTTONS_INDEX = 1
JOLTAGES_INDEX = 2

def solve(machine):
    min = 100000000000
    lights = machine[LIFHTS_INDEX]
    buttons = machine[BUTTONS_INDEX]

    all_combos = []
    for i in range(1, len(buttons)):
        combo = combinations(buttons, i)
        all_combos.append(combo)
    
    for combos in all_combos:
        for combo in combos:
            lights_number_of_presses = [0 for x in lights]
            len_of_combo = len(combo)
            for item in combo:
                for num in item: # ()
                    lights_number_of_presses[num] += 1
            actual_num_of_presses = [x % 2 for x in lights_number_of_presses]
            match = True
            for i in range(len(actual_num_of_presses)):
                if (lights[i] == "#" and actual_num_of_presses[i] == 0) or (lights[i] == "." and actual_num_of_presses[i] == 1):
                    match = False
                    break
            if match and len_of_combo < min:
                min = len_of_combo

    return min

def main():
    sum = 0
    machines = read_problem("input.txt")

    for m in machines:
        sum += solve(m)

    print("Answer {}".format(sum))


    

main()