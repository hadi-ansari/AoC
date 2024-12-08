def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    stripped_lines = []
    for l in lines:
        stripped_lines.append(l.strip())

    input_file.close()

    return stripped_lines
