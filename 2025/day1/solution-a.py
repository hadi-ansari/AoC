from reader import read_problem

def passes_zero():
    pass

def do_instruction(instruction, current_position):
    direction = instruction[0]
    distance = int(instruction[1:])

    if direction == "L":
        current_position = abs((current_position - distance) % 100)
    else:
        current_position = (current_position + distance) % 100

    return current_position

def main():
    password = 0
    current_position = 50
    instructions = read_problem("input.txt")

    for instruction in instructions:
        current_position = do_instruction(instruction, current_position)
        if current_position == 0:
            password +=1

    
    print("Password: {}".format(password))
        

main()