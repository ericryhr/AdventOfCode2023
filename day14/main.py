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

def move_rocks_row(row):
    prev_fixed = 0
    for i, rock in enumerate(row):
        if i == prev_fixed:
            if rock == 'O' or rock == '#': prev_fixed += 1
        else:
            if rock == 'O':
                row[prev_fixed] = 'O'
                row[i] = '.'
                while row[prev_fixed] != '.': 
                    prev_fixed += 1
                    if prev_fixed >= len(row): return
            elif rock == '#': prev_fixed = i + 1

def move_rocks(M):
    for row in M:
        move_rocks_row(row)

def transpose(M):
    return list(map(list, zip(*M)))

def reverse(M):
    return list(map(lambda x: list(reversed(x)), M))

def print_M(M):
    for m in M: print(m)
    print()

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    M = []
    for line in lines:
        M.append(list(line.strip()))
    Mt = list(map(list, zip(*M)))

    move_rocks(Mt)

    M = list(map(list, zip(*Mt)))
    result = calc_result(M)

    if result != -1:
        print("The solution to part one is: " + str(result))


def calc_diffs(M1, M2):
    diffs = 0
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            if M1[i][j] != M2[i][j]: diffs += 1
    return diffs


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    M = []
    previous_Ms = []
    for line in lines:
        M.append(list(line.strip()))

    found_cycle = False
    i = 0
    cycle = -1
    while not found_cycle:
        score = calc_result(M)
        # print(f'Cycle {i}, {score}')
        i += 1
        previous_Ms.append((M.copy(), score))
        # North
        Mnorth = transpose(M)
        # print('North')
        # print_M(Mnorth)
        move_rocks(Mnorth)
        # West
        Mwest = transpose(Mnorth)
        # print('West')
        # print_M(Mwest)
        move_rocks(Mwest)
        # South
        Msouth = transpose(Mwest)
        Msouth = reverse(Msouth)
        # print('South')
        # print_M(Msouth)
        move_rocks(Msouth)
        # East
        Meast = transpose(Msouth)
        Meast = reverse(Meast)
        # print('East')
        # print_M(Meast)
        move_rocks(Meast)
        # Return to normal
        M = transpose(Meast)
        M = reverse(M)
        M = transpose(M)
        M = reverse(M)
        
        for j, (prev_M, score) in enumerate(previous_Ms):
            if calc_diffs(prev_M, M) == 0: 
                found_cycle = True
                cycle = i-j
                # score = calc_result(M)
                # print(f'Cycle {i}, {score}')

    # print(f'Found cycle on iteration {i} with cycle {cycle}')
    it_objectiu = 1000000000
    cycle_og = (i-cycle)
    index = ((it_objectiu - cycle_og) % cycle) + cycle_og
    result = previous_Ms[index][1]

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day14/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
