"""
Author: Èric Ryhr Mateu
Day: 10
GitHub: https://github.com/ericryhr
"""

def search_S(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 'S':
                return (i, j)

valid_dirs = {
    'up': {'|': 'up', '7': 'left', 'F': 'right'},
    'down': {'|': 'down', 'J': 'left', 'L': 'right'},
    'left': {'-': 'left', 'L': 'up', 'F': 'down'},
    'right': {'-': 'right', 'J': 'up', '7': 'down'}
}

dirs = dict()
dirs['up'] = (-1, 0)
dirs['down'] = (1, 0)
dirs['left'] = (0, -1)
dirs['right'] = (0, 1)

def get_next_positions_from_S(M, start_pos):
    (i, j) = start_pos
    returning_pos = []
    returning_dirs = []

    for dir in dirs.keys():
        (off_i, off_j) = dirs[dir]
        (i2, j2) = (i+off_i, j+off_j)
        new_symbol = M[i2][j2]
        if new_symbol in valid_dirs[dir]:
            returning_dirs.append(dirs)
            returning_pos.append((i2, j2, valid_dirs[dir][new_symbol], new_symbol))
    
    if len(returning_pos) != 2:
        print(returning_pos)
        print('Something went wrong')
    
    replacement_symbol = 'S'
    if 'up' in returning_dirs:
        if 'down' in returning_dirs: replacement_symbol = '|'
        if 'left' in returning_dirs: replacement_symbol = 'J'
        if 'right' in returning_dirs: replacement_symbol = 'L'
    if 'down' in returning_dirs:
        if 'up' in returning_dirs: replacement_symbol = '|'
        if 'left' in returning_dirs: replacement_symbol = '7'
        if 'right' in returning_dirs: replacement_symbol = 'F'
    if 'right' in returning_dirs:
        if 'left' in returning_dirs: replacement_symbol = '-'
        if 'up' in returning_dirs: replacement_symbol = 'L'
        if 'down' in returning_dirs: replacement_symbol = 'F'
    if 'left' in returning_dirs:
        if 'right' in returning_dirs: replacement_symbol = '-'
        if 'up' in returning_dirs: replacement_symbol = 'J'
        if 'down' in returning_dirs: replacement_symbol = '7'
    return returning_pos[0], returning_pos[1], replacement_symbol

def get_next_pos(M, i, j, dir):
    (off_i, off_j) = dirs[dir]
    (i2, j2) = (i+off_i, j+off_j)
    new_symbol = M[i2][j2]
    new_dir = valid_dirs[dir][new_symbol]
    return (i2, j2, new_dir, new_symbol)


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    M = []
    for line in lines:
        M.append(line.strip())

    # Search S
    start_pos = search_S(M)

    # Get starting positions from S
    (i1, j1, dir1, _), (i2, j2, dir2, _), _ = get_next_positions_from_S(M, start_pos)
    result = 1

    while not (i1 == i2 and j1 == j2):
        (i1, j1, dir1, _) = get_next_pos(M, i1, j1, dir1)
        (i2, j2, dir2, _) = get_next_pos(M, i2, j2, dir2)
        result += 1

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    M = []
    for line in lines:
        M.append(line.strip())

    # for m in M: print(m)

    path = []
    new_path = []

    # Search S
    start_pos = search_S(M)

    # Get starting positions from S
    (i1, j1, dir1, sym1), (i2, j2, dir2, sym2), replacement_symbol = get_next_positions_from_S(M, start_pos)
    path.append((start_pos[0], start_pos[1], replacement_symbol))
    path.insert(0, (i1, j1, sym1))
    path.append((i2, j2, sym2))

    while not (i1 == i2 and j1 == j2):
        (i1, j1, dir1, sym1) = get_next_pos(M, i1, j1, dir1)
        (i2, j2, dir2, sym2) = get_next_pos(M, i2, j2, dir2)
        path.insert(0, (i1, j1, sym1))
        path.append((i2, j2, sym2))

    result = 0
    num_straight = 0
    num_curve = 0
    for k in range(len(path)-1):
        (_, _, sym) = path[k]
        if sym == '|' or sym == '-': num_straight+=1
        else: num_curve += 1
    
    num_closed = (num_curve+4)/2
    num_open = num_closed-4

    area_compensation = (0.25*num_closed) + (0.5*num_straight) + (0.75*num_open)

    for k in range(1, len(path)):
        (i1, j1, sym1) = path[k-1]
        (i2, j2, sym2) = path[k]
        area = (i2 + i1)*(j2 - j1)/2
        result += area
    result = int(abs(result) - area_compensation)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day10/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
