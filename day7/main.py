"""
Author: Èric Ryhr Mateu
Day: 7
GitHub: https://github.com/ericryhr
"""

import functools


types = [   'Repoker', 
            'Poker',
            'Full',
            'Trio',
            'Doble Parella',
            'Parella',
            'Null'  ]

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def get_type(hand):
    counts = []
    already_checked = []
    for c in hand:
        if not c in already_checked:
            counts.append(hand.count(c))
            already_checked.append(c)
        else: counts.append(-1)

    counts.sort(reverse=True)
    
    if counts[0] == 5: return 'Repoker'
    elif counts[0] == 4: return 'Poker'
    elif counts[0] == 3:
        if counts[1] == 2: return 'Full'
        else: return 'Trio'
    elif counts[0] == 2:
        if counts[1] == 2: return 'Doble Parella'
        else: return 'Parella'
    else: return 'Null'

def hand_sorting(hand_info_1, hand_info_2):
    (hand1, type1, _) = hand_info_1
    (hand2, type2, _) = hand_info_2

    index1 = types.index(type1)
    index2 = types.index(type2)

    if index1 < index2: return 1
    if index1 > index2: return -1

    for i in range(5):
        c1 = hand1[i]
        c2 = hand2[i]
        index1 = cards.index(c1)
        index2 = cards.index(c2)

        if index1 < index2: return 1
        if index1 > index2: return -1

    return 0

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    hands = []

    for line in lines:
        line = line.strip().split()
        hand, bid = line[0], int(line[1])
        hand_type = get_type(hand)
        hands.append((hand, hand_type, bid))

    hands.sort(key=functools.cmp_to_key(hand_sorting))

    # for hand in hands:
    #     print(hand)
    
    for i in range(len(hands)):
        (_, _, bid) = hands[i]
        result += bid*(i+1)

    if result != -1:
        print("The solution to part one is: " + str(result))


cards2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def get_type2(hand):
    counts = []
    already_checked = []
    for c in hand:
        if c == 'J': counts.append(0)
        else:
            if not c in already_checked:
                counts.append(hand.count(c))
                already_checked.append(c)
            else: counts.append(-1)

    counts.sort(reverse=True)
    # Sumem al primer tanets J com tenim
    counts[0] += counts.count(0)

    # print(counts)
    
    if counts[0] == 5: return 'Repoker'
    elif counts[0] == 4: return 'Poker'
    elif counts[0] == 3:
        if counts[1] == 2: return 'Full'
        else: return 'Trio'
    elif counts[0] == 2:
        if counts[1] == 2: return 'Doble Parella'
        else: return 'Parella'
    else: return 'Null'

def hand_sorting2(hand_info_1, hand_info_2):
    (hand1, type1, _) = hand_info_1
    (hand2, type2, _) = hand_info_2

    index1 = types.index(type1)
    index2 = types.index(type2)

    if index1 < index2: return 1
    if index1 > index2: return -1

    for i in range(5):
        c1 = hand1[i]
        c2 = hand2[i]
        index1 = cards2.index(c1)
        index2 = cards2.index(c2)

        if index1 < index2: return 1
        if index1 > index2: return -1

    return 0

def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    hands = []

    for line in lines:
        line = line.strip().split()
        hand, bid = line[0], int(line[1])
        hand_type = get_type2(hand)
        hands.append((hand, hand_type, bid))

    hands.sort(key=functools.cmp_to_key(hand_sorting2))

    # for hand in hands:
    #     print(hand)

    for i in range(len(hands)):
        (_, _, bid) = hands[i]
        result += bid*(i+1)

    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day7/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
