X = 0
Y = 1

def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()
    map = []

    inscructions = []
    reading_map = True
    counter = 0

    for l in lines:
        if l == "\n":
            counter += 1
            continue
        if counter >= 1:
            reading_map = False 
        if reading_map:
            map.append(list("".join(l.strip())))
        else:
            inscructions.append(list("".join(l.strip())))

    input_file.close()

    flat_final_instructions = [x for xs in inscructions for x in xs]

    return map, flat_final_instructions
