"""
Author: Èric Ryhr Mateu
Day: 11
GitHub: https://github.com/ericryhr
"""

import numpy as np
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    M = []
    for line in lines:
        M.append(line.strip())

    empty_rows = []
    for i, row in enumerate(M):
        if not '#' in row: empty_rows.append(i)
    
    empty_cols = []
    for j in range(len(M[0])):
        is_empty = True
        for i in range(len(M)):
            if M[i][j] == '#': is_empty = False
        if is_empty: empty_cols.append(j)

    galaxies = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == '#': galaxies.append(Point(i, j))

    # print(galaxies)

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            ga, gb = galaxies[i], galaxies[j]
            dist = 0
            minx, maxx = min(ga.x, gb.x), max(ga.x, gb.x)
            miny, maxy = min(ga.y, gb.y), max(ga.y, gb.y)
            for k in range(minx, maxx):
                if k in empty_rows: dist += 1
            for k in range(miny, maxy):
                if k in empty_cols: dist += 1
            dist += (abs(ga.x-gb.x) + abs(ga.y-gb.y))
            # print(i+1, ga, j+1, gb, dist)
            result += dist

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    M = []
    for line in lines:
        M.append(line.strip())

    empty_rows = []
    for i, row in enumerate(M):
        if not '#' in row: empty_rows.append(i)
    
    empty_cols = []
    for j in range(len(M[0])):
        is_empty = True
        for i in range(len(M)):
            if M[i][j] == '#': is_empty = False
        if is_empty: empty_cols.append(j)

    galaxies = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == '#': galaxies.append(Point(i, j))

    # print(galaxies)

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            ga, gb = galaxies[i], galaxies[j]
            dist = 0
            minx, maxx = min(ga.x, gb.x), max(ga.x, gb.x)
            miny, maxy = min(ga.y, gb.y), max(ga.y, gb.y)
            for k in range(minx, maxx):
                if k in empty_rows: dist += 999999
            for k in range(miny, maxy):
                if k in empty_cols: dist += 999999
            dist += (abs(ga.x-gb.x) + abs(ga.y-gb.y))
            # print(i+1, ga, j+1, gb, dist)
            result += dist

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day11/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
