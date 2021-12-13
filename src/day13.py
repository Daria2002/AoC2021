import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def part1(data, fold_instruction):
    direction = fold_instruction[0]
    value = int(fold_instruction[1])
    if direction == 'y':
        for i in range(value + 1, len(data)):
            for j in range(0, len(data[i])):
                if data[i][j] == '#':
                    data[value - 1 + (value + 1 - i)][j] = '#'
    elif direction == 'x':
        for i in range(0, len(data)):
            for j in range(value + 1, len(data[i])):
                if data[i][j] == '#':
                    data[i][value - 1 + (value + 1 - j)] = '#'
    counter = 0
    if direction == 'y':
        for i in range(0, value):
            row = []
            for j in range(0, len(data[i])):
                if data[i][j] == '#':
                    counter += 1
    elif direction == 'x':
        for i in range(0, len(data)):
            for j in range(0, value):
                if data[i][j] == '#':
                    counter += 1
    return counter

def process_data(rows):
    y_max = -1
    x_max = -1
    fold_instructions = []
    for row in rows:
        if row == '':
            continue
        if 'fold' in row:
            instruction = row.split(' ')[-1].split('=')
            fold_instructions.append((instruction[0], instruction[1]))
            continue
        x, y = row.split(',')
        x, y = int(x), int(y)
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
    data = [['.' for x in range(int(x_max) + 1)] for y in range(int(y_max) + 1)]
    for row in rows:
        if row == '':
            continue
        if 'fold' in row:
            continue
        x, y = row.split(',')
        x, y = int(x), int(y)
        data[y][x] = '#'
    return data, fold_instructions

if __name__ == '__main__':
    rows = get_all_input_rows('day13.txt')
    data, fold_instructions = process_data(rows)
    print(f'part1 = {part1(data, fold_instructions[0])}')