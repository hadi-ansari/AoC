def read_problem(file_name):
    input_file = open(file_name)

    lines = input_file.readlines()

    machines = []

    for l in lines:
        l = l.strip()

        lights = ""
        buttons = ""
        joltages = ""

        reading_lights = True
        reading_buttons = False
        reading_joltages = False
        current_str = ""

        for c in l:
            if reading_lights and c != "]": 
                current_str += c

            if reading_buttons and c != "{":
                current_str += c
            
            if reading_joltages and c != "}":
                current_str += c
            
            if reading_joltages and c == "}":
                current_str += c
                joltages = current_str

            if reading_buttons and c == "{":
                buttons = current_str
                reading_buttons = False
                reading_joltages = True
                current_str = ""
                current_str += c

            if c == "]":
                current_str += c
                lights = current_str
                current_str = ""
                reading_buttons = True
                reading_lights = False

            if c == " ":
                continue

        lights = list(lights[1:-1])
        buttons = buttons.split()
        temp_buttons = []
        for b in buttons: 
            temp_j = []
            for c in b:
                if c != "(" and c != ")" and c != ",":
                    temp_j.append(int(c))
            temp_buttons.append(temp_j)

        buttons = temp_buttons

        joltages = [int(x) for x in joltages[1:-1].split(",")]

        machines.append([lights, buttons, joltages])

    input_file.close()
    
    return machines