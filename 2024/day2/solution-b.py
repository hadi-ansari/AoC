from reader import read_problem
import copy
from collections import Counter

def is_safe_report(report_list):
    increasing = False
    decreasing = False

    if report_list[0] > report_list[1]:
        decreasing = True
    elif report_list[0] < report_list[1]:
        increasing = True
    else: 
        return False

    # print("list {} and increasing {}".format(report_list, increasing))
    for i in range(len(report_list) - 1):
        if abs(report_list[i] - report_list[i + 1]) > 3 or report_list[i] == report_list[i + 1]:
            # print("{} {}".format(report_list[i], report_list[i + 1]))

            return False
        
        if increasing and report_list[i] >= report_list[i + 1]:
            return False
        elif decreasing and report_list[i] <= report_list[i + 1]:
            # print("{} is greater than {}".format(report_list[i + 1], report_list[i]))
            return False
    return True

def is_safe_after_removal(report_list):
    for i in range(len(report_list)):
        temp_list = copy.deepcopy(report_list)
        temp_list.pop(i)
        if is_safe_report(temp_list):
            return True
            
    return False

def main():
    reports = read_problem("input.txt")
    total_safe = 0

    for report in reports:
        report_list = list(map(int, report.split()))

        if is_safe_report(report_list) or is_safe_after_removal(report_list):
            total_safe += 1

    print("total => ", total_safe)

main()
