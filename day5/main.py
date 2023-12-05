"""
Author: Èric Ryhr Mateu
Day: 5
GitHub: https://github.com/ericryhr
"""

import itertools

def parse_mapping(lines, mapping):
    lines = lines[1:]
    for line in lines:
        values = line.strip().split()
        mapping.append((values[0], values[1], values[2]))

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 10e30
    seeds = []
    seed_to_soil_mapping = []
    soil_to_fertilizer_mapping = []
    fertilizer_to_water_mapping = []
    water_to_light_mapping = []
    light_to_temperature_mapping = []
    temperature_to_humidity_mapping = []
    humidity_to_location_mapping = []
    
    seed_line = lines[0]
    seeds = seed_line.strip().split(': ')[1].split()
    lines = lines[2:]

    # Split lines by mappings
    mappings = [list(y) for x, y in itertools.groupby(lines, lambda z: z == '\n') if not x]
    parse_mapping(mappings[0], seed_to_soil_mapping)
    parse_mapping(mappings[1], soil_to_fertilizer_mapping)
    parse_mapping(mappings[2], fertilizer_to_water_mapping)
    parse_mapping(mappings[3], water_to_light_mapping)
    parse_mapping(mappings[4], light_to_temperature_mapping)
    parse_mapping(mappings[5], temperature_to_humidity_mapping)
    parse_mapping(mappings[6], humidity_to_location_mapping)

    mappings = [seed_to_soil_mapping, 
                soil_to_fertilizer_mapping, 
                fertilizer_to_water_mapping, 
                water_to_light_mapping, 
                light_to_temperature_mapping, 
                temperature_to_humidity_mapping, 
                humidity_to_location_mapping]
    
    for seed in seeds:
        currentValue = int(seed)
        for mapping in mappings:
            for (dest, source, rang) in mapping:
                (dest, source, rang) = (int(dest), int(source), int(rang))
                if currentValue in range(source, source + rang):
                    currentValue = currentValue + (dest - source)
                    break   # Check next mapping
        result = min(result, currentValue)


    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 10e30
    seeds = []
    seed_to_soil_mapping = []
    soil_to_fertilizer_mapping = []
    fertilizer_to_water_mapping = []
    water_to_light_mapping = []
    light_to_temperature_mapping = []
    temperature_to_humidity_mapping = []
    humidity_to_location_mapping = []
    
    seed_line = lines[0]
    seeds = seed_line.strip().split(': ')[1].split()
    seeds = list(zip(*[iter(seeds)] * 2))
    lines = lines[2:]

    # Split lines by mappings
    mappings = [list(y) for x, y in itertools.groupby(lines, lambda z: z == '\n') if not x]
    parse_mapping(mappings[0], seed_to_soil_mapping)
    parse_mapping(mappings[1], soil_to_fertilizer_mapping)
    parse_mapping(mappings[2], fertilizer_to_water_mapping)
    parse_mapping(mappings[3], water_to_light_mapping)
    parse_mapping(mappings[4], light_to_temperature_mapping)
    parse_mapping(mappings[5], temperature_to_humidity_mapping)
    parse_mapping(mappings[6], humidity_to_location_mapping)

    mappings = [seed_to_soil_mapping, 
                soil_to_fertilizer_mapping, 
                fertilizer_to_water_mapping, 
                water_to_light_mapping, 
                light_to_temperature_mapping, 
                temperature_to_humidity_mapping, 
                humidity_to_location_mapping]
    
    number_of_seeds_to_check = 0
    for (_, seed_rang) in seeds:
        number_of_seeds_to_check += int(seed_rang)
    print(f'Number of seeds to check: {number_of_seeds_to_check}')
    
    number_checked = 0
    for (s, seed_rang) in seeds:
        s = int(s)
        seed_rang = int(seed_rang)
        for seed in range(s, s+seed_rang):
            number_checked += 1
            if number_checked % 1e6 == 0: print(number_checked)
            currentValue = seed
            for mapping in mappings:
                for (dest, source, rang) in mapping:
                    (dest, source, rang) = (int(dest), int(source), int(rang))
                    if currentValue in range(source, source + rang):
                        currentValue = currentValue + (dest - source)
                        break   # Check next mapping
            result = min(result, currentValue)


    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day5/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
