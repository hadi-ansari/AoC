def read_problem(file_name):
    input_file = open(file_name)

    content = input_file.readlines()
    
    input_file.close()

    games = []
    for line in content:
        subsets = line.strip().split(":")[-1].split(";")
        formated_subsets = []
        for s in subsets:
            temp_subset = [0,0,0]  # RGB
            for t in s.strip().split(","):
                if "red" in t.strip():
                    temp_subset[0] = int(t.replace("red", "").strip())
                elif "green" in t.strip():
                    temp_subset[1] = int(t.replace("green", "").strip())
                else:
                    temp_subset[2] = int(t.replace("blue", "").strip())
            formated_subsets.append(temp_subset)
        
        games.append(formated_subsets)
    return games