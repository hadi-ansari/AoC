from reader import read_problem

A_REGISTER_KEY = "A"
B_REGISTER_KEY = "B"
C_REGISTER_KEY = "C"

def decimal_to_binary(num):
    binary = []
    div = num
    while True:
        if div < 2:
            binary.append(div)
            break
        
        remainder = div % 2
        binary.append(remainder)
        div = div // 2

    binary.reverse()
    return "".join(str(bit) for bit in binary)

def binary_to_decimal(num):
    res = 0
    num = num[::-1]
    for i in range(len(num)):
        res += (int(num[i]) * (2 ** i))
    return res

def get_combo_operand(registers, op):
    if op <= 3:
        return op
    if op == 4:
        return registers[A_REGISTER_KEY]
    elif op == 5:
        return registers[B_REGISTER_KEY]
    elif op == 6:
        return registers[C_REGISTER_KEY]
    elif op == 7:
        print("NOT VALID PROGRAM")
        return None

# 0
def adv(registers, op):
    registers[A_REGISTER_KEY] = registers[A_REGISTER_KEY] // (2 ** get_combo_operand(registers, op))

# 1
def bxl(registers, op):
    xor_result = ""
    first_num = decimal_to_binary(registers[B_REGISTER_KEY])
    second_num = decimal_to_binary(op)

    if len(first_num) > len(second_num):
        diff = len(first_num) - len(second_num)
        second_num = "0" * diff + second_num
    elif len(first_num) < len(second_num):
        diff = len(second_num) - len(first_num)
        first_num = "0" * diff + first_num

    for i in range(len(first_num)):
        if (first_num[i] != second_num[i]):
            xor_result += "1"
        else:
            xor_result += "0"
    
    registers[B_REGISTER_KEY] = binary_to_decimal(xor_result)

# 2
def bst(registers, op):
    registers[B_REGISTER_KEY] = get_combo_operand(registers, op) % 8
# 3
def jnz(registers, op):
    if registers[A_REGISTER_KEY] == 0:
        return None
    # jump op step forward
    return op

# 4
# ignore the operand
def bxc(registers, op):
    xor_result = ""
    first_num = decimal_to_binary(registers[B_REGISTER_KEY])
    second_num = decimal_to_binary(registers[C_REGISTER_KEY])

    if len(first_num) > len(second_num):
        diff = len(first_num) - len(second_num)
        second_num = "0" * diff + second_num
    elif len(first_num) < len(second_num):
        diff = len(second_num) - len(first_num)
        first_num = "0" * diff + first_num

    for i in range(len(first_num)):
        first_c = first_num[i]
        second_c = second_num[i]

        if first_c != second_c:
            xor_result += "1"
        else:
            xor_result += "0"

    registers[B_REGISTER_KEY] = binary_to_decimal(xor_result)

# 5
def out(registers, op):
    return(str(get_combo_operand(registers, op) % 8))

# 6
def bdv(registers, op):
    registers[B_REGISTER_KEY] = registers[A_REGISTER_KEY] // (2 ** get_combo_operand(registers, op))

# 7
def cdv(registers, op):
    registers[C_REGISTER_KEY] = registers[A_REGISTER_KEY] // (2 ** get_combo_operand(registers, op))

def run_program(registers, program):
    opcode_pointer = 0
    output = []
    while opcode_pointer < len(program):
        opcode = program[opcode_pointer]
        op = program[opcode_pointer + 1]
        opcode_increment = 2
        
        if opcode == 0: 
            adv(registers, op)
        elif opcode == 1:
            bxl(registers, op)
        elif opcode == 2:
            bst(registers, op)
        elif opcode == 3:
            next_pos = jnz(registers, op)
            if next_pos != None:
                opcode_pointer = next_pos
                continue
        elif opcode == 4:
            bxc(registers, op)
        elif opcode == 5:
            output.append(out(registers, op))
        elif opcode == 6:
            bdv(registers, op)
        elif opcode == 7:
            cdv(registers, op)

        opcode_pointer += opcode_increment
    return output

def main():
    registers, program = read_problem("input.txt")

    output = run_program(registers, program)
    for k in registers:
        print("key {} value {}".format(k, registers[k]))

    print(",".join(output))
main()