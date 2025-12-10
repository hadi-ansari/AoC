from z3 import *
from reader import read_problem

LIFHTS_INDEX = 0
BUTTONS_INDEX = 1
JOLTAGES_INDEX = 2

def get_counter_requirements(joltages, buttons_tuple):
    result = {}

    for i in range(len(joltages)):
        for j in range(len(buttons_tuple)):
            b = buttons_tuple[j]
            for counter_index in b:
                if counter_index == i:
                    if i in result:
                        result[i].append(j)
                    else:
                        result[i] = [j]
            
    return result

def sum(buttons, variables):
    res = variables[buttons[0]]
    for i in range(1, len(buttons)):
        res += variables[buttons[i]]

    return res

def solve(machine):
    joltages = machine[JOLTAGES_INDEX]
    buttons = machine[BUTTONS_INDEX]
    buttons_tuple = [tuple(x) for x in buttons]

    counter_requirement = get_counter_requirements(joltages, buttons_tuple)

    variables = []
    for i in range(len(buttons_tuple)):
        temp = Int(i)
        variables.append(temp)
  

    opt = Optimize()

    # Constraints
    for key in counter_requirement:
        buttons = counter_requirement[key]
        opt.add(sum(buttons, variables) == joltages[key])

    for v in variables:
        opt.add(v >= 0)

    
    total = variables[0]

    for i in range(1, len(variables)):
        total += variables[i]

    opt.minimize(total)
    opt.check()
    model = opt.model()
    min = model.evaluate(total)

    return str(min)


def main():
    answer = 0
    machines = read_problem("input.txt")

    for m in machines:
        res = solve(m)
        answer += int(res)

    print("Answer {}".format(answer))

main()