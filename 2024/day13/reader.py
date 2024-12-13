def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    claw_machines = []

    for i in range(0, len(lines), 4):
        a = (int(lines[i].strip().split("+")[1].split(",")[0]),int(lines[i].strip().split("+")[2].split(",")[0]))
        b = (int(lines[i + 1].strip().split("+")[1].split(",")[0]),int(lines[i + 1].strip().split("+")[2].split(",")[0]))
        p = (int(lines[i + 2].strip().split("=")[1].split(",")[0]), int(lines[i + 2].strip().split("=")[2]))
        
        claw_machines.append((a, b, p))
        

    input_file.close()

    return claw_machines
