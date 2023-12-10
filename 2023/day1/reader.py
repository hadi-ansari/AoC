def read_problem(file_name):
    input_file = open(file_name)

    content = input_file.readlines()
    
    input_file.close()

    return content