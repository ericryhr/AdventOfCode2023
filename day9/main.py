"""
Author: Èric Ryhr Mateu
Day: 9
GitHub: https://github.com/ericryhr
"""

def all_zeros(seq):
    for n in seq:
        if n != 0: return False
    return True

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    for line in lines:
        seqs = []
        line = line.strip()
        seqs.append(list(map(lambda x: int(x), line.split())))

        while not all_zeros(seqs[-1]):
            prev_seq = seqs[-1]
            new_seq = []
            for i in range(1, len(prev_seq)):
                new_seq.append(prev_seq[i]-prev_seq[i-1])
            seqs.append(new_seq)
        
        seqs.reverse()
        for i in range(len(seqs)):
            if i == 0: seqs[i].append(0)
            else: seqs[i].append(seqs[i][-1]+seqs[i-1][-1])
        
        result += seqs[-1][-1]
                   
    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION

    result = 0
    for line in lines:
        seqs = []
        line = line.strip()
        seqs.append(list(map(lambda x: int(x), line.split())))

        while not all_zeros(seqs[-1]):
            prev_seq = seqs[-1]
            new_seq = []
            for i in range(1, len(prev_seq)):
                new_seq.append(prev_seq[i]-prev_seq[i-1])
            seqs.append(new_seq)
        
        seqs.reverse()
        for i in range(len(seqs)):
            if i == 0: seqs[i].insert(0, 0)
            else: seqs[i].insert(0, seqs[i][0]-seqs[i-1][0])
        
        # print(seqs[-1][0])
        result += seqs[-1][0]



    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day9/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
