from reader import read_problem

def main():
    lines = read_problem("input.txt")

    problems =  {}
    for i in range(len(lines)):
        if i == len(lines) - 1:
            operations = [x for x in lines[i].strip().split()]
            for j in range(len(operations)):
                problems[j].append(operations[j])
            break

        nums = [int(x) for x in lines[i].strip().split()]
        for j in range(len(nums)):
            if j in problems:
                problems[j].append(nums[j])
            else:
                problems[j] = [nums[j]]


    sum = 0
    for key in problems:
        operator = problems[key][-1]
        problems[key].pop()

        if operator == "*":
            problem_sum = 1
        else:
            problem_sum = 0

        for i in range(len(problems[key])):
            if operator == "*":
                problem_sum *= problems[key][i]
            else: 
                 problem_sum += problems[key][i]
        sum += problem_sum


    print(sum)


main()