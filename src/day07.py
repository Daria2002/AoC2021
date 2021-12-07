import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def part1(positions):
    min_fuel = sys.maxsize
    max_position = max(positions)
    min_position = min(positions)
    for position1 in range(min_position, max_position + 1):
        fuel = 0
        for position2 in positions:
            if position1 == position2:
                continue
            fuel += abs(position1 - position2)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel

def part2(positions):
    min_fuel = sys.maxsize
    max_position = max(positions)
    min_position = min(positions)
    for position1 in range(min_position, max_position + 1):
        fuel = 0
        for position2 in positions:
            if position1 == position2:
                continue
            diff = abs(position1 - position2)
            tmp_fuel = (diff + 1) * diff // 2
            fuel += tmp_fuel
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel

if __name__ == '__main__':
    rows = get_all_input_rows('day07.txt')
    positions = [int(el) for el in rows[0].split(',')]
    print(f'Part 1: {part1(positions)}')
    print(f'Part 2: {part2(positions)}')