def read_problem(file_name):
    input_file = open(file_name)

    content = input_file.readlines()
    
    input_file.close()

    seeds = [eval(i) for i in content[0].split(":")[1].split()]
    dictionaries = {"seed_to_soil_map": [], "soil_to_fertilizer_map": [], "fertilizer_to_water_map": [], "water_to_light_map": [], "light_to_temperature_map": [], "temperature_to_humidity_map": [], "humidity_to_location_map": []}

    selected_map = ""
    for line in content:
        if len(line.split(":")[0].split()) == 3:
            l = [eval(i) for i in line.split(":")[0].split()]
            dictionaries[selected_map].append(l)
            continue
        if line.split(":")[0] == "seed-to-soil map":
            selected_map = "seed_to_soil_map"
        elif line.split(":")[0] == "soil-to-fertilizer map":
            selected_map = "soil_to_fertilizer_map"
        elif line.split(":")[0] == "fertilizer-to-water map":
            selected_map = "fertilizer_to_water_map"
        elif line.split(":")[0] == "water-to-light map":
            selected_map = "water_to_light_map"
        elif line.split(":")[0] == "light-to-temperature map":
            selected_map = "light_to_temperature_map"
        elif line.split(":")[0] == "temperature-to-humidity map":
            selected_map = "temperature_to_humidity_map"
        elif line.split(":")[0] == "humidity-to-location map":
            selected_map = "humidity_to_location_map"

    return seeds, dictionaries