def read_problem(file_name):
    input_file = open(file_name)

    content = input_file.readlines()

    input_file.close()

    hands = []

    for line in content:
        hands.append((line.split()[0], int(line.split()[1])))
    
    return hands