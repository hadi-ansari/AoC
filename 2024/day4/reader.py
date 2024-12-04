def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.strip())
    
    input_file.close()

    return stripped_lines
