def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    stripped_lines = []

    for l in lines:
        temp = list(l.strip())
        temp = [int(item) for item in temp]
        stripped_lines.append(temp)

    input_file.close()

    return stripped_lines
