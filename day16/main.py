"""
Author: Èric Ryhr Mateu
Day: 16
GitHub: https://github.com/ericryhr
"""

def calc_light(tile, dir, M, energized_tiles):
    (x, y) = tile
    if x < 0 or x >= len(M) or y < 0 or y >= len(M[0]): return

    (x_dir, y_dir) = dir
    energized_tiles[x][y] = True
    tile_type = M[x][y]

    if tile_type == '.': 
        (new_x, new_y) = (x+x_dir, y+y_dir)
        calc_light((new_x, new_y), dir, M, energized_tiles)
    elif tile_type == '/':
        print('Found /')
        (x_dir, y_dir) = (-1, -1)
        if y_dir == 1: (x_dir, y_dir) = (-1, 0)
        if y_dir == -1: (x_dir, y_dir) = (1, 0)
        if x_dir == -1: (x_dir, y_dir) = (0, 1)
        if x_dir == 1: (x_dir, y_dir) = (0, -1)
        (new_x, new_y) = (x+x_dir, y+y_dir)
        print(new_x, new_y)
        calc_light((new_x, new_y), (x_dir, y_dir), M, energized_tiles)
    elif tile_type == '\\':
        (x_dir, y_dir) = (-1, -1)
        if y_dir == 1: (x_dir, y_dir) = (1, 0)
        if y_dir == -1: (x_dir, y_dir) = (-1, 0)
        if x_dir == -1: (x_dir, y_dir) = (0, -1)
        if x_dir == 1: (x_dir, y_dir) = (0, 1)
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
        energized_tiles.append([False]*len(line))
    
    calc_light((0, 0), (0, 1), M, energized_tiles)

    for row in energized_tiles: print(row)

    for row in energized_tiles:
        for tile in row:
            result += tile

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION





    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day16/input2.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
