"""
Author: Èric Ryhr Mateu
Day: 3
GitHub: https://github.com/ericryhr
"""


def check_surroundings(matrix, i, j, number):
    number_length = len(number)
    for i2 in range(i-1, i+2):
        for j2 in range(j-1, j+number_length+1):
            if i2 < 0 or j2 < 0 or i2 >= len(matrix) or j2 >= len(matrix[0]): 
                continue
            if not matrix[i2][j2].isdigit() and matrix[i2][j2] != '.':
                return True
            
    return False


def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    matrix = []
    for line in lines:
        matrix.append(line.strip())

    # Get all the numbers
    numbers = []
    for i in range(len(matrix)):
        number = ''
        for j in range(len(matrix[i])):
            if number != '':
                if matrix[i][j].isdigit():
                    number += matrix[i][j]
                else:
                    number_length = len(number)
                    numbers.append((i, j-number_length, number))
                    number = ''
            else:
                if matrix[i][j].isdigit():
                    # Get digit value
                    number = matrix[i][j]
        if number != '':
            number_length = len(number)
            numbers.append((i, len(matrix[i])-number_length, number))
    
    # Check number surroundings
    for (i, j, number) in numbers:
        if check_surroundings(matrix, i, j, number):
            result += int(number)
        #     print('TRUE', (i, j, number), result)
        # else:
        #     print('FALSE', (i, j, number))


    if result != -1:
        print("The solution to part one is: " + str(result))


def check_gear(matrix, i, j, numbers, max_num_length):
    gearNumbers = []
    for i2 in range(i-1, i+2):
        for j2 in range(j-max_num_length, j+2):
            if i2 < 0 or j2 < 0 or i2 >= len(matrix) or j2 >= len(matrix[0]): 
                continue
            if (i2, j2) in numbers:
                # Check if number is short
                number = numbers[i2, j2]
                number_length = len(number)
                if j2 + number_length - 1 < j-1: continue

                gearNumbers.append(int(numbers[i2, j2]))
    
    if len(gearNumbers) == 2:
        # print(f'Gear in {(i, j)} is valid: {(gearNumbers[0], gearNumbers[1])}')
        return (gearNumbers[0], gearNumbers[1])
    else:
        # print(f'Gear in {(i, j)} is invalid: {gearNumbers}')
        return (-1, -1)

def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    matrix = []
    for line in lines:
        matrix.append(line.strip())

    # Get all the numbers
    numbers = dict()
    max_num_length = 0
    for i in range(len(matrix)):
        number = ''
        for j in range(len(matrix[i])):
            if number != '':
                if matrix[i][j].isdigit():
                    number += matrix[i][j]
                else:
                    number_length = len(number)
                    max_num_length = max(max_num_length, number_length)
                    numbers[(i, j-number_length)] = number
                    number = ''
            else:
                if matrix[i][j].isdigit():
                    # Get digit value
                    number = matrix[i][j]
        # Si arribem al final d'una linia comprovem que no estiguem comprovant un nombre
        if number != '':
            number_length = len(number)
            max_num_length = max(max_num_length, number_length)
            numbers[(i, len(matrix[i])-number_length)] = number

    # Check all gears
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '*':
                (num1, num2) = check_gear(matrix, i, j, numbers, max_num_length)
                if num1 != -1:
                    # Valid gear
                    result += num1*num2

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day3/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
