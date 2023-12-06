"""
Author: Èric Ryhr Mateu
Day: 6
GitHub: https://github.com/ericryhr
"""


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 1
    times = lines[0].strip().split(':')[1].strip().split()
    times = list(filter(lambda x: x != '', times))
    times = list(map(lambda x: int(x), times))
    distances = lines[1].strip().split(':')[1].strip().split()
    distances = list(filter(lambda x: x != '', distances))
    distances = list(map(lambda x: int(x), distances))

    for i in range(len(times)):
        num_ways = 0
        time = times[i]
        distance_to_beat = distances[i]

        for time_holding in range(0, time + 1):
            time_racing = time-time_holding
            speed = time_holding
            distance = speed * time_racing
            if distance > distance_to_beat: num_ways += 1

        result *= num_ways

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    time = int(lines[0].strip().split(':')[1].strip().replace(' ', ''))
    distance_to_beat = int(lines[1].strip().split(':')[1].strip().replace(' ', ''))
    
    for time_holding in range(0, time + 1):
        time_racing = time-time_holding
        speed = time_holding
        distance = speed * time_racing
        if distance > distance_to_beat: result += 1 

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day6/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
