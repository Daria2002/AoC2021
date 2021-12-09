import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def part1(rows, unique_len_dict):
    counter = 0
    for row in rows:
        parts = row.split(' | ')
        input = parts[0]
        output = parts[1]
        output_elements = output.split(' ')
        for element in output_elements:
            if len(element) in unique_len_dict:
                counter += 1
    return counter

def init_dict():
    d = {}
    d[0] = sorted(['c', 'a', 'g', 'e', 'd', 'b']) # [cagedb]
    d[1] = sorted(['a', 'b']) # [ab]
    d[2] = sorted(['g', 'c', 'd', 'f', 'a']) # [gcdfa]
    d[3] = sorted(['f', 'b', 'c', 'a', 'd']) # [fbcad]
    d[4] = sorted(['e', 'a', 'f', 'b']) # [eafb]
    d[5] = sorted(['c', 'd', 'f', 'b', 'e']) # [cdfbe]
    d[6] = sorted(['c', 'd', 'f', 'g', 'e', 'b']) # [cdfgeb]
    d[7] = sorted(['d', 'a', 'b']) # [dab]
    d[8] = sorted(['a', 'c', 'e', 'd', 'g', 'f', 'b']) # [acedgfb]
    d[9] = sorted(['c', 'e', 'f', 'a', 'b', 'd']) # [cefabd]
    return d

def get_key(element, signals):
    sorted_el = set(sorted(element))
    for key, value in signals.items():
        if value == sorted_el:
            return key
    return None

def map_signals(input_elements):
    signals = {}
    for input_el in input_elements:
        input_len = len(input_el)
        if input_len == 2:
            signals[1] = set(sorted(input_el))
        elif input_len == 3:
            signals[7] = set(sorted(input_el))
        elif input_len == 4:
            signals[4] = set(sorted(input_el))
        elif input_len == 7:
            signals[8] = set(sorted(input_el))
    for input_el in input_elements:
        input_len = len(input_el)
        # unique len, already in dict signals
        if input_len == 2 or input_len == 3 or input_len == 4 or input_len == 7:
            continue
        if input_len == 5:
            if (signals[4] - signals[1]).issubset(input_el): # 5
                signals[5] = set(sorted(input_el)) 
            elif (signals[7]).issubset(input_el): # 3
                signals[3] = set(sorted(input_el))
            else: # 2
                signals[2] = set(sorted(input_el))
        elif input_len == 6:
            if (signals[4] | signals[7]).issubset(input_el): # 9
                signals[9] = set(sorted(input_el))
            elif (signals[7]).issubset(input_el): # 0
                signals[0] = set(sorted(input_el))
            else: # 6
                signals[6] = set(sorted(input_el))
        else:
            print(f'somethings wrong with {input_el}, len = {input_len}, should be 5 or 6')
    return signals

def part2(rows):
    total_sum = 0
    for row in rows:
        parts = row.split(' | ')
        input = parts[0]
        output = parts[1]
        input_elements = input.split(' ')
        output_elements = output.split(' ')
        num = 0
        i = len(output_elements) - 1
        signals = map_signals(input_elements)
        for element in output_elements:
            num += pow(10, i) * get_key(element, signals)
            i -= 1
        total_sum += num
    return total_sum

def get_unique_len_dict(rows):
    d = init_dict()
    len_dict = {}
    for num, letters in d.items():
        if len(letters) not in len_dict:
            len_dict[len(letters)] = []
        len_dict[len(letters)].append(num)
    unique_len_dict = {}
    for len_, nums in len_dict.items():
        if len(nums) == 1:
            unique_len_dict[len_] = nums[0]
    return unique_len_dict

if __name__ == '__main__':
    rows = get_all_input_rows('day08.txt')
    unique_len_dict = get_unique_len_dict(rows)
    print(f'Part 1: {part1(rows, unique_len_dict)}')
    print(f'Part 2: {part2(rows)}')