"""
Author: Èric Ryhr Mateu
Day: 15
GitHub: https://github.com/ericryhr
"""


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    for line in lines:
        steps = line.strip().split(',')
        for step in steps:
            value = 0
            for c in step:
                value += ord(c)
                value *= 17
                value %= 256
            result += value


    if result != -1:
        print("The solution to part one is: " + str(result))

boxes = [dict() for i in range(256)]

def calc_value(h):
    value = 0
    for c in h:
        value += ord(c)
        value *= 17
        value %= 256
    return value

def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    for line in lines:
        steps = line.strip().split(',')
        for step in steps:
            if '=' in step:
                h, lens = step.split('=')
                box = calc_value(h)
                boxes[box][h] = int(lens)
            else:
                h = step.split('-')[0]
                box = calc_value(h)
                if h in boxes[box].keys():
                    del boxes[box][h]
    
    for i, box in enumerate(boxes):
        box_value = 1 + i
        for j, lens in enumerate(box.values()):
            result += box_value*(j+1)*lens


    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day15/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
