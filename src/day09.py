import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def part1(data):
    low_points = []
    data_matrix = []
    for row in data:
        row_elements = []
        for el in row:
            row_elements.append(int(el))
        data_matrix.append(row_elements)
    low_points_locations = []
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
            low_points_locations.append((row, col))
    risk_level = sum(low_points)
    return risk_level, low_points_locations, data_matrix

def get_basin_size_rec(data_matrix, row, col, prev_row, prev_col, visited, first = False):
    if row < 0 or row >= len(data_matrix) or col < 0 or col >= len(data_matrix[0]):
        return 0
    if visited[row][col] == 1:
        return 0
    if data_matrix[row][col] > data_matrix[prev_row][prev_col] or first:
        tmp_size = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i == -1 and j == -1) or (i == 1 and j == 1) or (i == -1 and j == 1) or (i == 1 and j == -1) or (i == 0 and j == 0):
                    continue 
                if i == prev_row and j == prev_col:
                    continue
                res_tmp = get_basin_size_rec(data_matrix, row + i, col + j, row, col, visited, False)
                if res_tmp != 0:
                    visited[row + i][col + j] = 1
                tmp_size += res_tmp
        return tmp_size + (1 if data_matrix[row][col] != 9 else 0)
    return 0

def part2(data_matrix, low_points_locations):
    basin_sizes = []
    visited = []
    for row in range(0, len(data_matrix)):
        tmp_visited = []
        for col in range(0, len(data_matrix[0])):
            tmp_visited.append(0)
        visited.append(tmp_visited)
    for row in range(0, len(data_matrix)):
        for col in range(0, len(data_matrix[0])):
            if (row, col) in low_points_locations:
                basin_size = get_basin_size_rec(data_matrix, row, col, row, col, visited, True) # don't count low point
                basin_sizes.append(basin_size)
    basin_sizes = sorted(basin_sizes, reverse=True)[:3]
    res = 1
    for s in basin_sizes:
        res *= s
    return res

if __name__ == '__main__':
    data = get_all_input_rows('day09.txt')
    risk_level, low_points_locations, data_matrix = part1(data)
    print(f'part 1: {risk_level}')
    print(f'part 2: {part2(data_matrix, low_points_locations)}')