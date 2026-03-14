def read_problem(file_name):
    input_file = open(file_name)

    content = input_file.readlines()

    races = []
    times = [int(t) for t in content[0].split()[1:]]
    distances = [int(t) for t in content[1].split()[1:]]
    
    for i in range(len(times)):
        races.append([times[i], distances[i]])

    input_file.close()

    return races