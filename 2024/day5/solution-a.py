from reader import read_problem

def main():
    rules, reports = read_problem("input.txt")

    lookup_dic = {}
    for rule_pair in rules:
        if rule_pair[0] in lookup_dic:
            lookup_dic[rule_pair[0]].append(rule_pair[1])
        else:
            lookup_dic[rule_pair[0]] = [rule_pair[1]]
    

    valid_reports = []
    for idx in range(len(reports)):
        is_valid = True
        for p_idx in range(len(reports[idx])):
            curr = reports[idx][p_idx]
            for j in range(p_idx - 1, -1, -1):
                if curr in lookup_dic and (reports[idx][j] in lookup_dic[curr]):
                    is_valid = False
            
        if is_valid:
            valid_reports.append(reports[idx])

    sum = 0
    for v in valid_reports:
        middleIndex = (len(v) - 1)//2
        sum += int(v[middleIndex])

    print("sum => ", sum)
main()