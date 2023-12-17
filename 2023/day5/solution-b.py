from reader import read_problem

def find_dest(source, map):
    for line in map:
        if not source in range(line[1], line[1] + line[2]):
            continue
        return source - line[1] + line[0]
    return source

def test(source_ranges, dest_map, cond = False):
    output_ranges = []
    queue = source_ranges
    while len(queue) > 0:
        l = queue.pop()
        range_found = False
        partially_range_found = False
        for l2 in dest_map:
            start_in_range = False
            end_in_range = False
            if l[0] in range(l2[0][0], l2[0][1] + 1):
                start_in_range = True
            if l[1] in range(l2[0][0], l2[0][1] + 1):
                end_in_range = True
            if start_in_range and end_in_range:
                temp = (l[0] - l2[0][0] + l2[1][0], l[1] - l2[0][0] + l2[1][0])
                output_ranges.append(temp)
                range_found = True
                break
            elif start_in_range or end_in_range:
                if start_in_range:
                    temp0 = (l[0], l2[0][1])
                    temp = (l[0] - l2[0][0] + l2[1][0], l2[0][1] - l2[0][0] + l2[1][0])
                    output_ranges.append(temp)
                    temp2 = (l2[0][1] + 1, l[1])
                    queue.append(temp2)
                else:
                    temp0 = (l2[0][0], l[1])
                    temp = (l2[1][0], l2[0][1] - l[1] + l2[1][0])
                    output_ranges.append(temp)
                    temp2 = (l[0], l2[0][0] - 1)
                    queue.append(temp2)
                partially_range_found = True
                break
            else:
                continue
        if partially_range_found:
            continue
        if not range_found:
            output_ranges.append(l)

    return output_ranges


def main():
    lowest_location = 100000000000
    seed_pairs, dictionaries = read_problem("input.txt")
    seed_ranges = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    for i in range(0, len(seed_pairs), 2):
        seed_ranges.append((seed_pairs[i], seed_pairs[i] + seed_pairs[i + 1]))
    
    for line in dictionaries["seed_to_soil_map"]:
        seed_to_soil.append(((line[1], line[1] + line[2] - 1), (line[0], line[0] + line[2] - 1)))

    for line in dictionaries["soil_to_fertilizer_map"]:
        soil_to_fertilizer.append(((line[1], line[1] + line[2] - 1), (line[0], line[0] + line[2] - 1)))

    for line in dictionaries["fertilizer_to_water_map"]:
        fertilizer_to_water.append(((line[1], line[1] + line[2] - 1), (line[0], line[0] + line[2] - 1)))

    for line in dictionaries["water_to_light_map"]:
        water_to_light.append(((line[1], line[1] + line[2] - 1), (line[0], line[0] + line[2] - 1)))

    for line in dictionaries["light_to_temperature_map"]:
        light_to_temperature.append(((line[1], line[1] + line[2] - 1), (line[0], line[0] + line[2] - 1)))

    for line in dictionaries["temperature_to_humidity_map"]:
        temperature_to_humidity.append(((line[1], line[1] + line[2] - 1), (line[0], line[0] + line[2] - 1)))

    for line in dictionaries["humidity_to_location_map"]:
        humidity_to_location.append(((line[1], line[1] + line[2] - 1), (line[0], line[0] + line[2] - 1)))

    
    

    seed_ranges.sort(key=lambda x: x[0])
    seed_to_soil.sort(key=lambda x: x[0])
    soil_to_fertilizer.sort(key=lambda x: x[0])
    fertilizer_to_water.sort(key=lambda x: x[0])
    water_to_light.sort(key=lambda x: x[0])
    light_to_temperature.sort(key=lambda x: x[0])
    temperature_to_humidity.sort(key=lambda x: x[0])
    humidity_to_location.sort(key=lambda x: x[0])

    soil_ranges = test(seed_ranges, seed_to_soil)

    fertilizer_ranges = test(soil_ranges, soil_to_fertilizer)

    water_ranges = test(fertilizer_ranges, fertilizer_to_water)

    light_ranges = test(water_ranges, water_to_light)

    temperature_ranges = test(light_ranges, light_to_temperature)

    humidity_ranges = test(temperature_ranges, temperature_to_humidity)

    location_ranges = test(humidity_ranges, humidity_to_location)

    for sr in location_ranges:
        if sr[0] < lowest_location:
            lowest_location = sr[0]

    print("Lowest location is: ", lowest_location)

    return

main()