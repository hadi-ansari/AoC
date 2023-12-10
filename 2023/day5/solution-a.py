from reader import read_problem

seeds, dictionaries = read_problem("input-real.txt")

lowest_location = 100000000000


def find_dest(source, map):
    found = False
    dest = -1
    for line in map:
        if line[1] > source or line[1] + line[2] < source:
            continue
        found = True
        dest = source - line[1] + line[0]
        break

    if found == False:
        return source
    return dest


for seed in seeds:
    soil = find_dest(seed, dictionaries["seed_to_soil_map"])
    fertilizer = find_dest(soil, dictionaries["soil_to_fertilizer_map"])
    water = find_dest(fertilizer, dictionaries["fertilizer_to_water_map"])
    light = find_dest(water, dictionaries["water_to_light_map"])
    temperature = find_dest(light, dictionaries["light_to_temperature_map"])
    humidity = find_dest(temperature, dictionaries["temperature_to_humidity_map"])
    location = find_dest(humidity, dictionaries["humidity_to_location_map"])
    if location <= lowest_location:
        lowest_location = location


print("lowest locations is: ", lowest_location)
    