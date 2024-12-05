def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.strip())
    
    input_file.close()

    rules = []
    reports = []

    rules_end = False
    for line in lines:
        if line[0]=="\n":
            rules_end = True
            continue
        if not rules_end:
            rules.append(line)
        else:
            reports.append(line)


    stripped_rules = []
    for r in rules:
       stripped_rules.append(r.strip().split("|"))

    stripped_reports = []
    for r in reports:
       stripped_reports.append(list(r.strip().split(',')))
            

    return stripped_rules, stripped_reports
