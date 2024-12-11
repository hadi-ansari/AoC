def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    stripped_lines = []

    for l in lines:
        temp = list(l.split())
        stripped_lines.append(temp)

    input_file.close()

    return stripped_lines[0]
