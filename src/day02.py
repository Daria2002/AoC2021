import os, sys
from typing import AsyncIterable

def part1():
    dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dir, '..\input\day02.txt')
    file = open(filename, 'r')
    rows = file.read().split('\n')
    horizontal = 0
    depth = 0
    for row in rows:
        direction = row.split(' ')[0]
        direction_value = int(row.split(' ')[1])
        if direction == 'forward':
            horizontal += direction_value
        elif direction == 'up':
            depth -= direction_value
        elif direction == 'down':
            depth += direction_value
        else:
            print(f'somethigs wrong with {row}')
    return horizontal * depth

def part2():
    dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dir, '..\input\day02.txt')
    file = open(filename, 'r')
    rows = file.read().split('\n')
    horizontal = 0
    depth = 0
    aim = 0
    for row in rows:
        direction = row.split(' ')[0]
        direction_value = int(row.split(' ')[1])
        if direction == 'forward':
            horizontal += direction_value
            depth += aim * direction_value
        elif direction == 'up':
            aim -= direction_value
        elif direction == 'down':
            aim += direction_value
        else:
            print(f'somethigs wrong with {row}')
    return horizontal * depth 

if __name__ == '__main__':
    res1 = part1()
    print(f'Part 1: {res1}')
    res2 = part2()
    print(f'Part 2: {res2}')