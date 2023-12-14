"""
Author: Èric Ryhr Mateu
Day: 14
GitHub: https://github.com/ericryhr
"""

def calc_result(M):
    result = 0
    for i, row in enumerate(M):
        for rock in row:
            if rock == 'O':
                result += (len(M) - i)
    return result

def move_rocks(M):
    for row in M:
        prev_fixed = 0
        for i, rock in enumerate(row):
            if rock == 'O':
                prev_fixed += 1
            elif rock == '#':

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    M = []
    for line in lines:
        M.append(list(line.strip()))
    Mt = list(map(list, zip(*M)))

    move_rocks(Mt)

    result = calc_result(Mt)

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION





    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day14/input2.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
