def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    coordinates = []

    for l in lines:
        l = l.strip().split(",")
        coordinate = [int(x) for x in l]
        coordinates.append(tuple((coordinate[1], coordinate[0])))

    input_file.close()
    
    return coordinates