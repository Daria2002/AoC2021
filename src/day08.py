import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def part1(rows, d):
    counter = 0
    len_dict = {}
    for num, letters in d.items():
        if len(letters) not in len_dict:
            len_dict[len(letters)] = []
        len_dict[len(letters)].append(num)
    unique_len_dict = {}
    for len_, nums in len_dict.items():
        if len(nums) == 1:
            unique_len_dict[len_] = nums[0]
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
    d[0] = ['a', 'b', 'c', 'e', 'f', 'g']
    d[1] = ['c', 'f']
    d[2] = ['a', 'c', 'd', 'e', 'g']
    d[3] = ['a', 'c', 'd', 'f', 'g']
    d[4] = ['b', 'c', 'd', 'f']
    d[5] = ['a', 'b', 'd', 'f', 'g']
    d[6] = ['a', 'b', 'd', 'e', 'f', 'g']
    d[7] = ['a', 'c', 'f']
    d[8] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    d[9] = ['a', 'b', 'c', 'd', 'f', 'g']
    return d

if __name__ == '__main__':
    d = init_dict()
    rows = get_all_input_rows('day08.txt')
    print(f'Part 1: {part1(rows, d)}')