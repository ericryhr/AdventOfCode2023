"""
Author: Èric Ryhr Mateu
Day: 19
GitHub: https://github.com/ericryhr
"""

import itertools
from dataclasses import dataclass

@dataclass
class Part:
    x: int
    m: int 
    a: int
    s: int

    def total_value(self) -> int:
        return self.x + self.m + self.a + self.s
    
    def value(self, letter) -> int:
        if letter == 'x': return self.x
        elif letter == 'm': return self.m
        elif letter == 'a': return self.a
        else: return self.s

def part1(lines):
    result = -1
    # PART 1 SOLUTION

    result = 0
    rules_lines, parts_lines = [list(y) for x, y in itertools.groupby(lines, lambda z: z == '\n') if not x]

    rules = dict()
    for line in rules_lines:
        line = line.strip()
        rule_name, rule = line.split('{')
        rule = rule[:-1]
        rules[rule_name] = []

        for step in rule.split(','):
            rules[rule_name].append(step)

    accepted_parts = []
    for part in parts_lines:
        part = part.strip()[1:-1]
        values = part.split(',')
        values = list(map(lambda x: int(x.split('=')[1]), values))
        part = Part(values[0], values[1], values[2], values[3])
        
        rejected = False
        accepted = False
        current_rule = 'in'
        while not (accepted or rejected):
            if current_rule == 'A': 
                accepted = True
                break
            elif current_rule == 'R':
                rejected = True
                break

            rule = rules[current_rule]
            for step in rule:
                if not ':' in step:
                    if step == 'A': accepted = True
                    elif step == 'R': rejected = True
                    else: current_rule = step
                else:
                    check, result_rule = step.split(':')
                    if '<' in check:
                        letter, number = check.split('<')
                        if part.value(letter) < int(number): 
                            current_rule = result_rule
                            break
                    else:
                        letter, number = check.split('>')
                        if part.value(letter) > int(number): 
                            current_rule = result_rule
                            break

        if accepted: accepted_parts.append(part)

    for part in accepted_parts: result += part.total_value()

    if result != -1:
        print("The solution to part one is: " + str(result))


def part2(lines):
    result = -1
    # PART 2 SOLUTION





    if result != -1:
        print("The solution to part two is: " + str(result))


def read_input(filename="day19/input.txt"):
    with open(filename, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    lines = read_input()

    part1(lines)
    part2(lines)
