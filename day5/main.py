"""
Author: Èric Ryhr Mateu
Day: 5
GitHub: https://github.com/ericryhr
"""

from numba import jit
from numba.typed import List
import itertools
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

def parse_mapping(lines, mapping):
    lines = lines[1:]
    for line in lines:
        values = line.strip().split()
        mapping.append((int(values[0]), int(values[1]), int(values[2])))

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
    seeds = list(map(lambda x: int(x), seeds))
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
        currentValue = seed
        for mapping in mappings:
            for (dest, source, rang) in mapping:
                (dest, source, rang) = (dest, source, rang)
                if currentValue in range(source, source + rang):
                    currentValue = currentValue + (dest - source)
                    break   # Check next mapping
        result = min(result, currentValue)


    if result != -1:
        print("The solution to part one is: " + str(result))

@jit(nopython=True)
def check_seeds(seeds, mappings):
    number_checked = 0
    result = 10e30
    for (s, seed_rang) in seeds:
        for seed in range(s, s+seed_rang):
            number_checked += 1
            # if number_checked % 1e6 == 0: print(number_checked)
            currentValue = seed
            for mapping in mappings:
                for (dest, source, rang) in mapping:
                    (dest, source, rang) = (dest, source, rang)
                    if currentValue in range(source, source + rang):
                        currentValue = currentValue + (dest - source)
                        break   # Check next mapping
            result = min(result, currentValue)
    return result

def part2(lines):
    result = -1
    # PART 2 SOLUTION

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
    seeds = list(map(lambda x: int(x), seeds))
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
    
    mapping_list = List()
    for mapping in mappings:
        mapping_list.append(mapping)
    
    number_of_seeds_to_check = 0
    for (_, seed_rang) in seeds:
        number_of_seeds_to_check += seed_rang
    # print(f'Number of seeds to check: {number_of_seeds_to_check}')
    
    result = check_seeds(seeds, mapping_list)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day5/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
