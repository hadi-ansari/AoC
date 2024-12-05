from reader import read_problem
import copy

def bubble_sort(lookup_dic, report):
    temp = copy.deepcopy(report)

    for k in range(len(report) - 1):
        for i in range(len(report) - k - 1):

            if temp[i+1] in lookup_dic and temp[i] in lookup_dic[temp[i+1]]:
                first = temp[i+1]
                second = temp[i]
                temp[i] = first
                temp[i+1] = second

    return temp


def main():
    rules, reports = read_problem("input.txt")

    lookup_dic = {}
    for rule_pair in rules:
        if rule_pair[0] in lookup_dic:
            lookup_dic[rule_pair[0]].append(rule_pair[1])
        else:
            lookup_dic[rule_pair[0]] = [rule_pair[1]]
    

    invalid_reports = []
    for idx in range(len(reports)):
        is_valid = True
        for p_idx in range(len(reports[idx])):
            curr = reports[idx][p_idx]
            for j in range(p_idx - 1, -1, -1):
                if not is_valid:
                    break
                if curr in lookup_dic and (reports[idx][j] in lookup_dic[curr]):
                    is_valid = False
                    invalid_reports.append(reports[idx])
                    break
            
    fixed_reports = []
    for i in invalid_reports:
       fixed_reports.append(bubble_sort(lookup_dic, i))
    
    sum = 0
    for v in fixed_reports:
        middleIndex = (len(v) - 1)//2
        sum += int(v[middleIndex])

    print("sum => ", sum)

    
main()