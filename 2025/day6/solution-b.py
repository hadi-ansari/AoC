from reader import read_problem

def main():
    lines = read_problem("input.txt")

    problems_operation =  {}
    fromatted_problems = {}
    new_problems = {}
    max_len = {}
    for i in range(len(lines)):
        if i == len(lines) - 1:
            operations = [x for x in lines[i].strip().split()]
            for j in range(len(operations)):
                problems_operation[j].append(operations[j])
            break

        nums = [x for x in lines[i].strip().split()]
        fromatted_problems[i] = nums
        for j in range(len(nums)):
            if j in problems_operation:
                problems_operation[j].append(nums[j])
            else:
                problems_operation[j] = [nums[j]]


    max_len = {}
    for key in fromatted_problems:
        p = fromatted_problems[key]
        for j in range(len(p)):
            current_num = p[j]
            if j in max_len:
                if len(current_num) > max_len[j]:
                    max_len[j] = len(current_num)
            else:
                max_len[j] = len(current_num)


    for i in range(len(lines)):
        current = 0
        next = -1
        l = lines[i]
        if i == len(lines) - 1:
            break
        for j in range(len(max_len)):
            next = max_len[j] + current
            num = l[current: next]
            current = next + 1
            if j in new_problems:
                new_problems[j].append(num)
            else:
                new_problems[j] = [num]


    sum = 0
    for key in new_problems:
        current_problem = new_problems[key]
        operator = problems_operation[key][-1]
        if operator == "*":
            problem_sum = 1
        else:
            problem_sum = 0
        nums = []
        for j in range(len(current_problem[0])):
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