def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()
    
    ranges = []
    items = []

    items_mode = False
    for l in lines:
        if l.strip() == "":
            items_mode = True
            continue
        if items_mode:
            items.append(int(l.strip()))
            continue

        start = int(l.split("-")[0])
        last = int(l.split("-")[1])

        ranges.append((start, last))
    
    input_file.close()

    return ranges, items