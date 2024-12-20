X = 0
Y = 1

def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    reading_program = False
    program = None
    registers = {}

    for l in lines:
        stripped_line = l.strip()
        if stripped_line == "":
            reading_program = True
            continue
        if reading_program:
            temp = stripped_line.split()[1].split(",")
            program = [int(x) for x in temp]
        else:
            register = stripped_line.split()[1][0]
            value = int(stripped_line.split()[2])
            registers[register] = value
    
    input_file.close()

    return registers, program