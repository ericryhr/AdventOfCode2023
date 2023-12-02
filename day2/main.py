"""
Author: Èric Ryhr Mateu
Day: 2
GitHub: https://github.com/ericryhr
"""

import re


numRed = 12
numGreen = 13
numBlue = 14

def checkGame(game):
    throws = game.split('; ')
    for throw in throws:
        dices = throw.split(', ')
        for dice in dices:
            num = int(dice.split(' ')[0])
            color = dice.split(' ')[1]
            match color:
                case 'red': 
                    if num > numRed: return False
                case 'green': 
                    if num > numGreen: return False
                case 'blue': 
                    if num > numBlue: return False
    return True

def part1(lines):
    result = -1
    # PART 1 SOLUTION
    result = 0
    mainPattern = r"Game (\d+): (.+\n)"

    for line in lines:
        mainMatch = re.match(mainPattern, line)
        if mainMatch:
            gameId = int(mainMatch.group(1))
            game = mainMatch.group(2)
            if checkGame(game):
                result += gameId

    if result != -1:
        print("The solution to part one is: " + str(result))


def gamePower(game):
    minRed = minGreen = minBlue = 0
    throws = game.split('; ')
    for throw in throws:
        dices = throw.split(', ')
        for dice in dices:
            num = int(dice.split(' ')[0].strip())
            color = dice.split(' ')[1].strip()
            match color:
                case 'red': 
                    if num > minRed: minRed = num
                case 'green': 
                    if num > minGreen: minGreen = num
                case 'blue': 
                    if num > minBlue: minBlue = num
    # print(f'Red: {minRed}, Green: {minGreen}, Blue: {minBlue}')
    return minRed * minBlue * minGreen

def part2(lines):
    result = -1
    # PART 2 SOLUTION
    result = 0
    mainPattern = r"Game (\d+): (.+\n)"

    for line in lines:
        mainMatch = re.match(mainPattern, line)
        if mainMatch:
            gameId = int(mainMatch.group(1))
            game = mainMatch.group(2)
            power = gamePower(game)
            # print(f'Game {gameId}: {power} \n')
            result += power

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day2/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
