"""
Author: Èric Ryhr Mateu
Day: 1
GitHub: https://github.com/ericryhr
"""


def part1(lines):
    suma = 0

    for line in lines:
        num1 = num2 = 0
        # Primer nombre
        for i in line:
            if i.isdigit():
                num1 = int(i)
                break
        # Segon nombre
        for i in reversed(line):
            if i.isdigit():
                num2 = int(i)
                break
        
        suma += (10*num1 + num2)

    print(f'La solució de la part 1 és {suma}')


numSequences = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letterSequences = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def part2(lines):
    suma = 0

    for line in lines:
        num1 = num2 = 0
        index = -1
        #Primer nombre
        lowest_index = 100000000
        for i in range(0, len(numSequences)):
            index = line.find(numSequences[i])
            if index != -1 and index < lowest_index:
                num1 = int(i)
                lowest_index = index

        for i in range(0, len(letterSequences)):
            index = line.find(letterSequences[i])
            if index != -1 and index < lowest_index:
                num1 = i+1
                lowest_index = index

        # Segon nombre
        highest_index = -1
        index = -1
        for i in range(0, len(numSequences)):
            check_index = 0
            while line.find(numSequences[i], check_index) != -1:
                index = line.find(numSequences[i], check_index)
                check_index = index + 1
            if index != -1 and index > highest_index:
                num2 = i
                highest_index = index

        for i in range(0, len(letterSequences)):
            check_index = 0
            while line.find(letterSequences[i], check_index) != -1:
                index = line.find(letterSequences[i], check_index)
                check_index = index + 1
            if index != -1 and index > highest_index:
                num2 = i+1
                highest_index = index
        
        # print(num1, num2, (10*num1 + num2))

        suma += (10*num1 + num2)

    print(f'La solució de la part 2 és {suma}')


def read_input(filename="day1/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
