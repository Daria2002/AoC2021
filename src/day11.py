import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def has_flashing_octopus(data):
    for row in data:
        for el in row:
            if el > 9:
                return True
    return False

def part1(rows, steps):
    data = []
    for row in rows:
        row_arr = []
        for el in row:
            row_arr.append(int(el))
        data.append(row_arr)
    total_flashes = 0
    for step in range(1, steps + 1):
        for row in range(0, len(data)):
            for col in range(0, len(data[row])):
                data[row][col] += 1
        while has_flashing_octopus(data):
            for row in range(0, len(data)):
                for col in range(0, len(data[row])):
                    if data[row][col] > 9:
                        data[row][col] *= (-1)
                        for row_offset in [-1, 0, 1]:
                            for col_offset in [-1, 0, 1]:
                                if row + row_offset >= 0 and row + row_offset < len(data) and col + col_offset >= 0 and col + col_offset < len(data[row]):
                                    if data[row + row_offset][col + col_offset] < 0:
                                        continue
                                    data[row + row_offset][col + col_offset] += 1
        for row in range(0, len(data)):
            for col in range(0, len(data[row])):
                if data[row][col] < 0:
                    data[row][col] = 0
                    total_flashes += 1
    return total_flashes

def are_all_zeros(data):
    for row in data:
        for el in row:
            if el != 0:
                return False
    return True

def part2(rows):
    data = []
    for row in rows:
        row_arr = []
        for el in row:
            row_arr.append(int(el))
        data.append(row_arr)
    total_flashes = 0
    step = 0
    while not are_all_zeros(data):
        for row in range(0, len(data)):
            for col in range(0, len(data[row])):
                data[row][col] += 1
        while has_flashing_octopus(data):
            for row in range(0, len(data)):
                for col in range(0, len(data[row])):
                    if data[row][col] > 9:
                        data[row][col] *= (-1)
                        for row_offset in [-1, 0, 1]:
                            for col_offset in [-1, 0, 1]:
                                if row + row_offset >= 0 and row + row_offset < len(data) and col + col_offset >= 0 and col + col_offset < len(data[row]):
                                    if data[row + row_offset][col + col_offset] < 0:
                                        continue
                                    data[row + row_offset][col + col_offset] += 1
        for row in range(0, len(data)):
            for col in range(0, len(data[row])):
                if data[row][col] < 0:
                    data[row][col] = 0
                    total_flashes += 1
        step += 1
    return step

if __name__ == '__main__':
    rows = get_all_input_rows('day11.txt')
    print(f'Part 1: {part1(rows, 100)}')
    print(f'Part 2: {part2(rows)}')