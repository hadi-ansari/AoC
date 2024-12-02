def read_problem(file_name):
    input_file = open(file_name)

    reports = input_file.readlines()
  
    
    input_file.close()

    return reports