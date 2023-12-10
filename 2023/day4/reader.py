def read_problem(file_name):
    input_file = open(file_name)

    content = input_file.readlines()
    
    input_file.close()

    cards = []
    for i in range(len(content)):
        winning = content[i].split("|")[0].split(":")[1].split()
        owned = content[i].split("|")[1].split()
        cards.append([winning, owned, 1])

    return cards