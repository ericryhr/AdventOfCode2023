"""
Author: Èric Ryhr Mateu
Day: 16
GitHub: https://github.com/ericryhr
"""

import sys
import copy

sys.setrecursionlimit(1000000)

dir_hash = {    -2: 1, 
                -1: 2,
                1: 4,
                2: 8}

def calc_light(tile, dir, M, energized_tiles):
    (x, y) = tile
    (x_dir, y_dir) = dir
    if x < 0 or x >= len(M) or y < 0 or y >= len(M[0]): return

    tile_type = M[x][y]
    
    dir_val = x_dir + y_dir*2
    if dir_hash[dir_val] & energized_tiles[x][y]: return
    else: energized_tiles[x][y] += dir_hash[dir_val]

    # print(x, y)
    # for row in energized_tiles: print(row)

    if tile_type == '.': 
        (new_x, new_y) = (x+x_dir, y+y_dir)
        calc_light((new_x, new_y), dir, M, energized_tiles)
    elif tile_type == '/':
        if y_dir == 1: (x_dir, y_dir) = (-1, 0)
        elif y_dir == -1: (x_dir, y_dir) = (1, 0)
        elif x_dir == -1: (x_dir, y_dir) = (0, 1)
        elif x_dir == 1: (x_dir, y_dir) = (0, -1)
        (new_x, new_y) = (x+x_dir, y+y_dir)
        calc_light((new_x, new_y), (x_dir, y_dir), M, energized_tiles)
    elif tile_type == '\\':
        if y_dir == 1: (x_dir, y_dir) = (1, 0)
        elif y_dir == -1: (x_dir, y_dir) = (-1, 0)
        elif x_dir == -1: (x_dir, y_dir) = (0, -1)
        elif x_dir == 1: (x_dir, y_dir) = (0, 1)
        (new_x, new_y) = (x+x_dir, y+y_dir)
        calc_light((new_x, new_y), (x_dir, y_dir), M, energized_tiles)
    elif tile_type == '|':
        if y_dir == 0:
            (new_x, new_y) = (x+x_dir, y+y_dir)
            calc_light((new_x, new_y), dir, M, energized_tiles)
        else:
            calc_light((x-1, y), (-1, 0), M, energized_tiles)
            calc_light((x+1, y), (1, 0), M, energized_tiles)
    elif tile_type == '-':
        if x_dir == 0:
            (new_x, new_y) = (x+x_dir, y+y_dir)
            calc_light((new_x, new_y), dir, M, energized_tiles)
        else:
            calc_light((x, y-1), (0, -1), M, energized_tiles)
            calc_light((x, y+1), (0, 1), M, energized_tiles)




def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    M = []
    energized_tiles = []
    for line in lines:
        line = line.strip()
        M.append(list(line))
        energized_tiles.append([0]*len(line))

    # for row in energized_tiles: print(row)
    
    calc_light((0, 0), (0, 1), M, energized_tiles)

    # print('Result')
    # for row in energized_tiles: print(row)

    for row in energized_tiles:
        for tile in row:
            if tile != 0: result += 1

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    M = []
    energized_tiles = []
    for line in lines:
        line = line.strip()
        M.append(list(line))
        energized_tiles.append([0]*len(line))

    # Left column
    for i in range(len(M)):
        partial_result = 0
        partial_energized_tiles = copy.deepcopy(energized_tiles)
        calc_light((i, 0), (0, 1), M, partial_energized_tiles)

        for row in partial_energized_tiles:
            for tile in row:
                if tile != 0: partial_result += 1

        result = max(partial_result, result)

    # Right column
    for i in range(len(M)):
        partial_result = 0
        partial_energized_tiles = copy.deepcopy(energized_tiles)
        calc_light((i, len(M[i])-1), (0, -1), M, partial_energized_tiles)

        for row in partial_energized_tiles:
            for tile in row:
                if tile != 0: partial_result += 1

        result = max(partial_result, result)

    # Upper row
    for j in range(len(M[0])):
        partial_result = 0
        partial_energized_tiles = copy.deepcopy(energized_tiles)
        calc_light((0, j), (1, 0), M, partial_energized_tiles)

        for row in partial_energized_tiles:
            for tile in row:
                if tile != 0: partial_result += 1

        result = max(partial_result, result)

    # Bottom row
    for j in range(len(M[0])):
        partial_result = 0
        partial_energized_tiles = copy.deepcopy(energized_tiles)
        calc_light((len(M)-1, j), (-1, 0), M, partial_energized_tiles)

        for row in partial_energized_tiles:
            for tile in row:
                if tile != 0: partial_result += 1

        result = max(partial_result, result)

    # print('Result')
    # for row in energized_tiles: print(row) 

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day16/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
