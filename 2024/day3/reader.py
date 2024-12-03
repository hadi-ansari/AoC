def read_problem(file_name):
    input_file = open(file_name)

    curropted_memory = input_file.readlines()
  
    
    input_file.close()

    return curropted_memory