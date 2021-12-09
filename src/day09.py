import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def part1(data):
    low_points = []
    data_matrix = []
    for row in data:
        row_elements = []
        for el in row:
            row_elements.append(el)
        data_matrix.append(row_elements)
    for row in range(0, len(data)):
        for col in range(0, len(data[0])):
            if row - 1 >= 0 and data[row - 1][col] <= data[row][col]:
                continue
            if row + 1 < len(data) and data[row + 1][col] <= data[row][col]:
                continue
            if col - 1 >= 0 and data[row][col - 1] <= data[row][col]:
                continue
            if col + 1 < len(data[0]) and data[row][col + 1] <= data[row][col]:
                continue
            low_points.append(int(data[row][col]) + 1) # for each low point add 1
    risk_level = sum(low_points)
    return risk_level

def part2(data):
    return 0

if __name__ == '__main__':
    data = get_all_input_rows('day09.txt')
    print(f'part 1: {part1(data)}')
    print(f'part 2: {part2(data)}')