def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()
    presents = []
    regions = []
    temp_shape = []
    shape_idx = None

    reading_presents = True
    for l in lines:
        l = l.strip()
        if l == "":
            presents.append(temp_shape)
            temp_shape = []
            continue
        elif "x" in l:
            reading_presents = False
        elif ":" in l:
            continue
        if reading_presents:
            temp_shape.append(list(l))
        else:
            x = (l.split(":")[0]).split("x")[0]
            y = (l.split(":")[0]).split("x")[1]
            temp_presents = [int(x) for x in l.split(":")[1].split()]
            region = {"size": (int(y),int(x)), "presents": temp_presents}
            regions.append(region)
        
    input_file.close()

    return {"shapes": presents, "regions": regions}