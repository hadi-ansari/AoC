from reader import read_problem
import re
import copy
from math import lcm

def main():
    content = read_problem("input-b.txt")
    instructions = content[0].split()[0]
    road_graph = {}

    current_positions = []
    for i in range(len(content)):
        if not i < 2:
            splited_line = content[i].split("=")
            key = splited_line[0].strip()
            road_graph[key] = tuple(re.findall('[A-Z1-9]{3}', splited_line[1]))
            if key[-1] == "A":
                current_positions.append(key)

    # This list contains all steps needed to get to destinations ending with Z for
    # each position starts with A. It seems that in order to get to another Z it takes same
    # amount of steps
                
    steps_to_z = []
    for cp in current_positions:
        # print("Finding steps for {}".format(cp))
        current_position = cp
        steps = 0
        while True:
            cond = False
            for instruction in instructions:
                if current_position[-1] == 'Z':
                    # print("{} => {}  steps taken: {}".format(cp, current_position, steps))
                    steps_to_z.append(steps)
                    cond = True
                    break

                if current_position[-1] != 'Z':
                    if instruction == "L":
                        # print("from {} = {} left => {} ". format(current_position, road_graph[current_position], road_graph[current_position][0]))
                        current_position = road_graph[current_position][0]
                    else:
                        # print("from {} = {} right => {} ". format(current_position, road_graph[current_position], road_graph[current_position][1]))
                        current_position = road_graph[current_position][1]
                    steps += 1
            if cond:
                # print("=" * 50)
                break
    # Least common multiple of all steps
    print(lcm(steps_to_z[0], steps_to_z[1], steps_to_z[2], steps_to_z[3], steps_to_z[4], steps_to_z[5]))


main()