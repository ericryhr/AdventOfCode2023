"""
Author: Èric Ryhr Mateu
Day: 18
GitHub: https://github.com/ericryhr
"""


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    trajectory = []

    for line in lines:
        dir, movement, color = line.strip().split()
        movement = int(movement)
        trajectory.append((dir, movement))

    current_pos = [0, 0]
    result = 0
    total_movement = 0
    for dir, movement in trajectory:
        area = 0
        total_movement += movement
        if dir == 'U': current_pos[0] += movement
        elif dir == 'D': current_pos[0] -= movement
        elif dir == 'L': 
            area -= movement * current_pos[0]
            current_pos[1] -= movement
        elif dir == 'R': 
            area += movement * current_pos[0]
            current_pos[1] += movement
        # print(dir, movement, area)
        result += area

    result += int(total_movement/2) + 1

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    trajectory = []

    for line in lines:
        _, _, color = line.strip().split()
        color = color[2:-1]
        movement = int(color[0:5], 16)
        dir = int(color[-1])
        if dir == 0: dir = 'R'
        elif dir == 1: dir = 'D'
        elif dir == 2: dir = 'L'
        elif dir == 3: dir = 'U'
        # print(dir, movement)
        trajectory.append((dir, movement))

    current_pos = [0, 0]
    result = 0
    total_movement = 0
    for dir, movement in trajectory:
        area = 0
        total_movement += movement
        if dir == 'U': current_pos[0] += movement
        elif dir == 'D': current_pos[0] -= movement
        elif dir == 'L': 
            area -= movement * current_pos[0]
            current_pos[1] -= movement
        elif dir == 'R': 
            area += movement * current_pos[0]
            current_pos[1] += movement
        # print(dir, movement, area)
        result += area

    result += int(total_movement/2) + 1

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day18/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
