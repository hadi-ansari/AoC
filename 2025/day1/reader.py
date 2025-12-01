def read_problem(file_name):
    input_file = open(file_name)

    instructions = input_file.readlines()
    
    
    for i in range(len(instructions)):
        instructions[i] = instructions[i].strip()
    input_file.close()

    return instructions