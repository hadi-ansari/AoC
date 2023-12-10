import re

input_file = open("input-real.txt")

content = input_file.readlines()

input_file.close()

instructions = content[0].split()[0]

road_graph = {}

for i in range(len(content)):
    if not i < 2:
        splited_line = content[i].split("=")
        road_graph[splited_line[0].strip()] = tuple(re.findall('[A-Z]{3}', splited_line[1]))

current_position = 'AAA'
steps = 0
while current_position != 'ZZZ':
    for instruction in instructions:
        if instruction == "L":
            current_position = road_graph[current_position][0]
        else:
            current_position = road_graph[current_position][1]
        steps += 1
    
print(steps)