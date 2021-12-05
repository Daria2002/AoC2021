import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import * 

def part1():
    return solve_matrix(skip_diagonals=True)

def part2():
    return solve_matrix(skip_diagonals=False)

def solve_matrix(skip_diagonals):
    rows = get_all_input_rows('day05.txt')
    num_of_rows = 0
    num_of_cols = 0
    for row in rows:
        coordinates1, coordinates2 = row.split(' -> ')
        x1, y1 = coordinates1.split(',')
        x2, y2 = coordinates2.split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if num_of_cols < x1:
            num_of_cols = x1
        if num_of_rows < y1:
            num_of_rows = y1
        if num_of_cols < x2:
            num_of_cols = x2
        if num_of_rows < y2:
            num_of_rows = y2
    matrix = [[0] * (num_of_cols + 1) for i in range(num_of_rows + 1)]
    for row in rows:
        coordinates1, coordinates2 = row.split(' -> ')
        x1, y1 = coordinates1.split(',')
        x2, y2 = coordinates2.split(',')
        x1_int, y1_int, x2_int, y2_int = int(x1), int(y1), int(x2), int(y2)

        x1 = x1_int if x1_int < x2_int else x2_int
        y1 = y1_int if y1_int < y2_int else y2_int
        x2 = x2_int if x2_int > x1_int else x1_int
        y2 = y2_int if y2_int > y1_int else y1_int

        if x1 == x2:
            for i in range(y1, y2+1):
                matrix[i][x1] += 1
        elif y1 == y2:
            for i in range(x1, x2+1):
                matrix[y1][i] += 1
        elif skip_diagonals:
            continue
        else: # Diagonal has 4 cases
            if x1_int < x2_int and y1_int < y2_int:
                j = y1_int
                for i in range(x1_int, x2_int+1):
                    matrix[j][i] += 1
                    j += 1
            elif x1_int < x2_int and y1_int > y2_int:
                j = y1_int
                for i in range(x1_int, x2_int+1):
                    matrix[j][i] += 1
                    j -= 1
            elif x1_int > x2_int and y1_int < y2_int:   
                j = y1_int
                for i in range(x1_int, x2_int - 1, -1):
                    matrix[j][i] += 1
                    j += 1
            elif x1_int > x2_int and y1_int > y2_int:
                j = y1_int
                for i in range(x1_int, x2_int - 1, -1):
                    matrix[j][i] += 1
                    j -= 1
    count = 0
    for row in matrix:
        for el in row:
            if el > 1:
                count += 1
    return count

if __name__ == "__main__":
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')