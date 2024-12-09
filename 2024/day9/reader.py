def read_problem(file_name):
    input_file = open(file_name)


    lines = input_file.readlines()

    list_line = list("".join(lines))

    list_line_number = [int(item) for item in list_line]
    

    input_file.close()

    return list_line_number
