def read_problem(file_name):
    input_file = open(file_name)

    content = input_file.readlines()

    input_file.close()

    for i in range(len(content)):
        content[i] = list(map(int, content[i].strip().split()))

    return content