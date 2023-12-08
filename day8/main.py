"""
Author: Èric Ryhr Mateu
Day: 8
GitHub: https://github.com/ericryhr
"""

from functools import reduce
from math import lcm


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    instructions = lines[0].strip()
    start_node, end_node = 'AAA', 'ZZZ'
    nodes = dict()
    lines = lines[2:]
    for line in lines:
        line = line.strip().split(' = ')
        origin = line[0]
        dest = line[1].replace('(', '').replace(')', '').split(', ')
        left, right = dest[0], dest[1]
        nodes[origin] = (left, right)

    current_node = start_node
    instruction_index = 0
    while current_node != end_node:
        instruction = instructions[instruction_index]
        if instruction == 'L':
            current_node = nodes[current_node][0]
        elif instruction == 'R':
            current_node = nodes[current_node][1]
        else: print('MISTAKE PARSING')

        result += 1
        instruction_index += 1
        if instruction_index >= len(instructions): instruction_index = 0

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    instructions = lines[0].strip()
    nodes = dict()
    lines = lines[2:]
    for line in lines:
        line = line.strip().split(' = ')
        origin = line[0]
        dest = line[1].replace('(', '').replace(')', '').split(', ')
        left, right = dest[0], dest[1]
        nodes[origin] = (left, right)

    start_nodes = list(filter(lambda n: n[-1] == 'A', nodes.keys()))
    node_vals = []
    for start_node in start_nodes:
        current_node = start_node
        instruction_index = 0
        node_count = 0
        while current_node[-1] != 'Z':
            instruction = instructions[instruction_index]
            if instruction == 'L':
                current_node = nodes[current_node][0]
            elif instruction == 'R':
                current_node = nodes[current_node][1]
            else: print('MISTAKE PARSING')

            node_count += 1
            instruction_index += 1
            if instruction_index >= len(instructions): instruction_index = 0
        node_vals.append(node_count)

    result = lcm(*node_vals)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day8/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
