def read_problem(file_name):
    input_file = open(file_name)

    line = input_file.readlines()
    
    ranges = line[0].split(",")
    
    input_file.close()

    return ranges