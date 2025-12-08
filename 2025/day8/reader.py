def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()


    junction_boxes = []

    for l in lines:
        l = l.strip().split(",")
        coordinate = [int(x) for x in l]
        junction_boxes.append(tuple(coordinate))

    input_file.close()
    
    return junction_boxes