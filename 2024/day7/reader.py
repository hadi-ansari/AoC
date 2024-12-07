def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    content = []
    for equation in lines:
        res = equation.split(":")[0]
        numbers = equation.split(":")[1].split()
        temp = []
        temp.append(res)
        temp.append(numbers)
        content.append(temp)

    input_file.close()

    return content
