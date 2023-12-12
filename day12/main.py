"""
Author: Èric Ryhr Mateu
Day: 12
GitHub: https://github.com/ericryhr
"""

# from numba import jit
# from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
# import warnings

# warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
# warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

# @jit(nopython=True)
def check_answer(springs, info):
    if sum(info) != springs.count('#'): return False
    groups = ''.join(springs).split('.')
    groups = list(filter(lambda x: x != '', groups))

    for i, group in enumerate(groups):
        if i >= len(info): return False
        if len(group) != info[i]: return False
    return True

def backtracking(springs, info, i):
    if sum(info) < springs.count('#'): return 0

    if i >= len(springs):
        return 1 if check_answer(springs, info) else 0
    
    while springs[i] != '?': 
        i+=1
        if i >= len(springs):
            return 1 if check_answer(springs, info) else 0
    b1 = springs.copy()
    b2 = springs.copy()
    b1[i] = '.'
    b2[i] = '#'
    return backtracking(b1, info, i+1) + backtracking(b2, info, i+1)

def gen_all_possible_combinations(springs, info):
    i = 0
    while springs[i] != '?': 
        i+=1
        if i >= len(springs):
            return 1 if check_answer(springs, info) else 0
    b1 = springs.copy()
    b2 = springs.copy()
    b1[i] = '.'
    b2[i] = '#'
    return backtracking(b1, info, i+1) + backtracking(b2, info, i+1)

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    for line in lines:
        line = line.strip().split()
        springs = list(line[0])
        info = list(map(lambda x: int(x), line[1].split(',')))
        r = gen_all_possible_combinations(springs, info)
        # print(r)
        result += r

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION





    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day12/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
