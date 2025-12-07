from reader import read_problem

def main():
    lines = read_problem("input.txt")

    problems_operation =  {}
    fromated_lines = {}
    problems = {}
    max_len = {}
    problem_count = len(lines[0].strip().split())

    # Read operations and lines of numbers and store them in fromated_lines and problems_operation dictionaries
    for i in range(len(lines)):
        if i == len(lines) - 1:
            operations = [x for x in lines[i].strip().split()]
            for j in range(len(operations)):
                problems_operation[j] = operations[j]
            break

        nums = [x for x in lines[i].strip().split()]
        fromated_lines[i] = nums


    # Find max length of each problem (each column) and store them in max_len dictionary
    for key in fromated_lines:
        p = fromated_lines[key]
        for j in range(len(p)):
            current_num = p[j]
            if j in max_len:
                if len(current_num) > max_len[j]:
                    max_len[j] = len(current_num)
            else:
                max_len[j] = len(current_num)


    # Slice the colums based on max lenght of that problem (column) and store them in problems dictionary
    for i in range(len(lines)):
        current = 0
        next = -1
        l = lines[i]
        if i == len(lines) - 1:
            break

        for j in range(problem_count):
            next = max_len[j] + current
            num = l[current: next]
            current = next + 1
            if j in problems:
                problems[j].append(num)
            else:
                problems[j] = [num]


    sum = 0
    for key in problems:
        current_problem = problems[key]
        operator = problems_operation[key]
        if operator == "*":
            problem_sum = 1
        else:
            problem_sum = 0
        nums = []
        for j in range(max_len[key]):
            temp_str = ""
            for i in range(len(current_problem)):
                current_num = current_problem[i]
                current_digit = current_problem[i][j]
                if current_digit == " ":
                    continue
                else:
                    temp_str += current_digit
            nums.append(temp_str)
        
        for n in nums:
            if operator == "*":
                problem_sum *= int(n)
            else:
                problem_sum += int(n)
        sum += problem_sum
        

    print(sum)


main()