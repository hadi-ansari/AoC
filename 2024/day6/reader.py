def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    final_lines = []
    for line in lines:
        temp = []
        stripped_line = line.strip()
        for c in stripped_line:
            temp.append(c)
        final_lines.append(temp)

    input_file.close()

    return final_lines
