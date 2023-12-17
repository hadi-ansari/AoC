def read_problem(file_name):
    input_file = open(file_name)

    content = input_file.readlines()
    
    input_file.close()

    times = content[0].split(":")[-1].strip().split()
    distances = content[1].split(":")[-1].strip().split()

    return times, distances