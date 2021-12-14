import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def part1(polymer_template, pair_insertion_rules, steps):
    for step in range(0, steps):
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
    pairs = []
    count_elements = {}
    count_pairs = {}
    for i in range(0, len(polymer_template) - 1):
        pairs.append(polymer_template[i:i+2])
        count_pairs[polymer_template[i:i+2]] = 1
        if polymer_template[i] not in count_elements:
            count_elements[polymer_template[i]] = 0
        if polymer_template[i + 1] not in count_elements:
            count_elements[polymer_template[i + 1]] = 0
        count_elements[polymer_template[i]] += 1
    if polymer_template[-1] not in count_elements:
        count_elements[polymer_template[-1]] = 0
    count_elements[polymer_template[-1]] += 1
    for step in range(0, steps):
        new_count_pairs = {}
        print(f'Step {step}')
        for pair_, pair_counter in count_pairs.items():
            insertion_el = pair_insertion_rules[pair_]
            if insertion_el not in count_elements:
                count_elements[insertion_el] = 0
            if pair_[0] + insertion_el not in new_count_pairs:
                new_count_pairs[pair_[0] + insertion_el] = 0
            if insertion_el + pair_[1] not in new_count_pairs:
                new_count_pairs[insertion_el + pair_[1]] = 0
            new_count_pairs[pair_[0] + insertion_el] += pair_counter
            new_count_pairs[insertion_el + pair_[1]] += pair_counter
            count_elements[insertion_el] += pair_counter
        count_pairs = dict(new_count_pairs)
    max_val, min_val = 0, sys.maxsize
    for el, count_val in count_elements.items():
        if count_val > max_val:
            max_val = count_val
        if count_val < min_val:
            min_val = count_val
    return max_val - min_val

if __name__ == '__main__':
    rows = get_all_input_rows('day14.txt')
    polymer_template, pair_insertion_rules = rows[0], {row.split(' -> ')[0]: row.split(' -> ')[1] for row in rows[2:]}
    print(f'Part 1: {part1(polymer_template, pair_insertion_rules, 10)}')
    print(f'Part 2: {part2(polymer_template, pair_insertion_rules, 40)}')