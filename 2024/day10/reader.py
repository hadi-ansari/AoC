def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    stripped_lines = []

    for l in lines:
        temp = list(l.strip())

        temp2 = []
        for i in temp:
            if i == ".":
                temp2.append(-2)
            else:
                temp2.append(int(i))
        stripped_lines.append(temp2)

    input_file.close()

    return stripped_lines
