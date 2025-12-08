from reader import read_problem
from functools import cmp_to_key
import math

X_INDEX = 0
Y_INDEX = 1
Z_INDEX = 2

distances = {}

def sort_by_distance(junction_boxes):
    for i in range(len(junction_boxes)):
        for j in range(len(junction_boxes)):
            if i == j or (junction_boxes[i], junction_boxes[j]) in distances or (junction_boxes[j], junction_boxes[i]) in distances:
                continue
            distance = math.sqrt((junction_boxes[i][X_INDEX] - junction_boxes[j][X_INDEX])**2 + (junction_boxes[i][Y_INDEX] - junction_boxes[j][Y_INDEX])**2 + (junction_boxes[i][Z_INDEX] - junction_boxes[j][Z_INDEX])**2)
            distances[(junction_boxes[i], junction_boxes[j])] = distance
    
    distances_list = []
    for key in distances:
        distances_list.append([key, distances[key]])
    
    sorted_distances_list = sorted(distances_list, key=cmp_to_key(lambda a, b: a[1] - b[1]))
    sorted_distances_list.reverse()
    return sorted_distances_list

def main():
    junction_boxes = read_problem("input.txt")

    sorted_distances_list = sort_by_distance(junction_boxes)
    circuits = []

    while True:
        current = sorted_distances_list.pop()

        c1 = current[0][0]
        c2 = current[0][1]
        found = False

        c1_in_another_circuit = False
        c1_index = None
        c1_circuit = []

        c2_in_another_circuit = False
        c2_index = None
        c2_circuit = []

        for j in range(len(circuits)):
            current_circuit = circuits[j]

            if c1 in current_circuit and c2 in current_circuit:
                found = True
                break
            if c1 in current_circuit and c2 not in current_circuit:
                c1_in_another_circuit = True
                c1_index = j
                c1_circuit = current_circuit
                found = True
            if c1 not in current_circuit and c2 in current_circuit:
                c2_in_another_circuit = True
                c2_index = j
                c2_circuit = current_circuit
                found = True

            # last iteration
            if j == len(circuits) - 1:
                if c1_in_another_circuit and c2_in_another_circuit:
                    merge_circuit = circuits[c1_index] + circuits[c2_index]
                    temp = []
                    for k in range(len(circuits)):
                        if k != c1_index and k != c2_index:
                            temp.append(circuits[k])
                    temp.append(merge_circuit)
                    
                    circuits = temp
                elif c1_in_another_circuit and not c2_in_another_circuit:
                    c1_circuit.append(c2)
                    circuits.pop(c1_index)
                    circuits.append(c1_circuit)
                elif not c1_in_another_circuit and c2_in_another_circuit:
                    c2_circuit.append(c1)
                    circuits.pop(c2_index)
                    circuits.append(c2_circuit)

        if not found:
            circuits.append([c1, c2])

        if len(circuits) == 1 and len(circuits[0]) == len(junction_boxes):
            print("Answer is {}".format(c1[X_INDEX] * c2[X_INDEX]))
            return
    

main()