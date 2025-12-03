def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()
    
    banks = []

    for l in lines:
        banks.append(l.strip())
    
    input_file.close()

    return banks