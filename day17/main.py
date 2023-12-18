"""
Author: Èric Ryhr Mateu
Day: 17
GitHub: https://github.com/ericryhr
"""

MAX = 1000000000000

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(current_pos, M, positions_checked):
    (x, y) = current_pos

    # Check end
    if x == len(M)-1 and y == len(M[0])-1: return M[x][y]

    vals = []

    for (x_dir, y_dir) in dirs:
        (x_new, y_new) = (x+x_dir, y+y_dir)
        if x_new >= 0 and y_new >= 0 and x_new < len(M) and y_new < len(M[0]) and not positions_checked[x_new][y_new]:
            positions_checked[x_new][y_new] = True
            vals.append(dfs((x_new, y_new), M, positions_checked))
            positions_checked[x_new][y_new] = False

    if len(vals) == 0: return MAX
    else:
        return min(vals) + M[x][y]


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    M = []
    positions_checked = []
    for line in lines:
        line = list(map(lambda x: int(x), line.strip()))
        M.append(line)
        positions_checked.append([False]*len(line))

    result = dfs((0, 0), M, positions_checked)

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION





    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day17/input2.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
