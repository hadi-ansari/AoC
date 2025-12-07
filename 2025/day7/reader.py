def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()


    manifold = []

    for l in lines:
        temp = []
        l = l.strip()
        for c in l:
            temp.append(c)
        manifold.append(temp)

    input_file.close()
    
    return manifold