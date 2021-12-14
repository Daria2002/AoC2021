import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def part1(polymer_template, pair_insertion_rules, steps):
    for step in range(0, steps):
        print(f'Step {step}')
        result = ""
        for i in range(0, len(polymer_template) - 1, 1):
            if i == 0:
                result += polymer_template[i]
            result += pair_insertion_rules[polymer_template[i:i+2]] + polymer_template[i+1]
        polymer_template = result
    dict_count = {}
    for el in result:
        if el not in dict_count:
            dict_count[el] = 0
        dict_count[el] += 1
    max_count = 0
    min_count = len(result)
    for el, count in dict_count.items():
        if max_count < count:
            max_count = count
        if min_count > count:
            min_count = count
    return max_count - min_count

def part2(polymer_template, pair_insertion_rules, steps):
    return part1(polymer_template, pair_insertion_rules, steps)

if __name__ == '__main__':
    rows = get_all_input_rows('day14.txt')
    polymer_template, pair_insertion_rules = rows[0], {row.split(' -> ')[0]: row.split(' -> ')[1] for row in rows[2:]}
    print(f'Part 1: {part1(polymer_template, pair_insertion_rules, 10)}')
    print(f'Part 2: {part2(polymer_template, pair_insertion_rules, 40)}')