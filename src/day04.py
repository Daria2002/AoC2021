import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
from helper.funcs import *

def resolve_matrix(matrix, nums):
    matrix_sum = sum(sum(row) for row in matrix)
    marked_cells = [[0] * len(matrix[0]) for i in range(len(matrix))]
    for i in range(0, len(nums)):
        marked = False
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] == nums[i]:
                    marked_cells[row][col] = 1
                    matrix_sum -= nums[i]
                    marked = True
                    break
            if marked:
                break
        for row in range(0, len(matrix)):
            done = True
            for col in range(0, len(matrix[0])):
                if marked_cells[row][col] == 0:
                    done = False
                    break
            if done:
                return i, nums[i], matrix_sum
        for col in range(0, len(matrix[0])):
            done = True
            for row in range(0, len(matrix)):
                if marked_cells[row][col] == 0:
                    done = False
                    break
            if done:
                return i, nums[i], matrix_sum
    return -1, -1, -1

def part1(rows):
    nums = [int(el) for el in rows[0].split(',')]
    matrix_arr = []
    tmp_matrix = []
    for i in range(2, len(rows)):
        if rows[i] == '':
            matrix_arr.append(tmp_matrix)
            tmp_matrix = []
            continue
        elements = rows[i].split(' ')
        matrix_row = []
        for el in elements:
            if el != '':
                matrix_row.append(int(el))
        tmp_matrix.append(matrix_row)
    matrix_arr.append(tmp_matrix)

    min_i = len(nums) + 1
    min_num = -1
    min_sum = -1
    for matrix in matrix_arr:
        i, num, matrix_sum = resolve_matrix(matrix, nums)
        if i < min_i:
            min_i = i
            min_num = num
            min_sum = matrix_sum
    return min_num * min_sum

if __name__ == "__main__":
    rows = get_all_input_rows('day04.txt')
    print(f'part1 = {part1(rows)}')