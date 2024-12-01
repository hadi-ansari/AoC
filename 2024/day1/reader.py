def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()
    first_col = []
    second_col = []


    for line in lines:
        first_col.append(line.split()[0])
        second_col.append(line.split()[1])
    
    input_file.close()

    return first_col, second_col