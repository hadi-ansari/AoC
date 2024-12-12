def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    map = []

    for l in lines:
        map.append(list(l.strip()))

        

    input_file.close()

    return map
