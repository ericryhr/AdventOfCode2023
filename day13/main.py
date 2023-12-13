"""
Author: Èric Ryhr Mateu
Day: 13
GitHub: https://github.com/ericryhr
"""

import itertools

def check_simmetry(M, ind):
    for i in range(0, ind+1):
        ind_down = ind-i
        ind_up = ind+i+1
        if ind_up >= len(M): return True
        if M[ind_down] != M[ind_up]: return False
    return True

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    patterns = [list(y) for x, y in itertools.groupby(lines, lambda z: z == '\n') if not x]

    for pattern in patterns:
        M = []
        for line in pattern:
            M.append(line.strip())
        Mt = [''.join(s) for s in zip(*M)]
        
        for i in range(len(M)-1):
            if check_simmetry(M, i):
                result += (i+1)*100
                break

        for i in range(len(Mt)-1):
            if check_simmetry(Mt, i): 
                result += (i+1)
                break


    if result != -1:
        print("The solution to part one is: " + str(result))


def count_simmetry(M, ind):
    count = 0
    for i in range(0, ind+1):
        ind_down = ind-i
        ind_up = ind+i+1
        if ind_up >= len(M): return count
        for j in range(len(M[ind_down])):
            if M[ind_down][j] != M[ind_up][j]: count += 1
    return count

def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    patterns = [list(y) for x, y in itertools.groupby(lines, lambda z: z == '\n') if not x]

    for pattern in patterns:
        M = []
        for line in pattern:
            M.append(line.strip())
        Mt = [''.join(s) for s in zip(*M)]
        
        for i in range(len(M)-1):
            count = count_simmetry(M, i)
            if count == 1:
                result += (i+1)*100
                break

        for i in range(len(Mt)-1):
            count = count_simmetry(Mt, i)
            if count == 1:
                result += (i+1)
                break


    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day13/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
