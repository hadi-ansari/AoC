from reader import read_problem
    

def do_instruction(instruction, current_position):
    direction = instruction[0]
    distance = int(instruction[1:])
    passed_zero_times = 0
    
    if distance == 100:
        return current_position, 1
    

    temp_position = current_position
    if direction == "L":
       for i in range(distance):
            temp_position = abs((temp_position - 1) % 100)
            if temp_position == 0:
                passed_zero_times += 1
    else:
         for i in range(distance):
              temp_position = (temp_position + 1) % 100
              if temp_position == 0:
                 passed_zero_times += 1

    return temp_position, passed_zero_times

def main():
    password = 0
    current_position = 50
    instructions = read_problem("input.txt")

    for instruction in instructions:
        current_position, time_passed_zero = do_instruction(instruction, current_position)

        password += time_passed_zero

    
    print("Password: {}".format(password))
        

main()