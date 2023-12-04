"""
Author: Èric Ryhr Mateu
Day: 4
GitHub: https://github.com/ericryhr
"""


def part1(lines):
    result = -1
    # PART 1 SOLUTION
    
    result = 0
    for line in lines:
        card = line.strip()
        numbers = card.split(': ')[1]
        numbers = numbers.split(' | ')
        winning_numbers = numbers[0].split(' ')
        winning_numbers = list(filter(lambda x: x != '', winning_numbers))
        my_numbers = numbers[1].split(' ')
        my_numbers = list(filter(lambda x: x != '', my_numbers))
        points = 0
        for number in my_numbers:
            if number in winning_numbers:
                if points == 0: points = 1
                else: points *= 2

        # print(f'{card} obtained {points} points')

        result += points


    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    cards = []
    for line in lines:
        card = line.strip()
        card_id = int(card.split(': ')[0].split(' ')[-1])
        numbers = card.split(': ')[1]
        numbers = numbers.split(' | ')
        winning_numbers = numbers[0].split(' ')
        winning_numbers = list(filter(lambda x: x != '', winning_numbers))
        my_numbers = numbers[1].split(' ')
        my_numbers = list(filter(lambda x: x != '', my_numbers))
        cards.append((card_id, winning_numbers, my_numbers))
    
    card_queue = []
    for card in cards:
        # print(card)
        card_queue.append(card)

    while len(card_queue) > 0:
        result += 1
        (card_id, winning_numbers, my_numbers) = card_queue.pop()
        num_cards = 0
        for number in my_numbers:
            if number in winning_numbers: num_cards += 1

        for i in range(card_id, card_id + num_cards):
            card_queue.append(cards[i])

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day4/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
