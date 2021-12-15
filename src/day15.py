import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *
import networkx as nx

def get_risk(aoc_input):
    chitons = {(i,j):c for i,row in enumerate(aoc_input) for j,c in enumerate(row)}
    neighbors=lambda x,y:[(x+dx,y+dy)for dx,dy in[(-1,0),(1,0),(0,-1),(0,1)]if(x+dx,y+dy)in chitons]
    cave = nx.DiGraph()
    cave.add_edges_from(((x,y), n, {'weight':chitons[n]}) for x,y in chitons for n in neighbors(x,y))
    return nx.dijkstra_path_length(cave,(0,0),(len(aoc_input)-1,len(aoc_input[0])-1),weight='weight')

def get_neighbors(x, y, matrix_len):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = [(x + dx, y + dy) for dx, dy in offsets if (x + dx >= 0 and x + dx < matrix_len and y + dy >= 0 and y + dy < matrix_len)] 
    return neighbors

def part1(matrix):
    weights = {}
    matrix_len = len(matrix)
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            weights[(i,j)] = c
    cave = nx.DiGraph()
    for x, y in weights:
        neighbors = get_neighbors(x, y, matrix_len)
        for neighbor in neighbors:
            neighbor_weight = weights[neighbor]
            cave.add_edge((x, y), neighbor, weight=neighbor_weight)
    return nx.dijkstra_path_length(cave, (0, 0), (len(matrix) - 1, len(matrix[0]) - 1), weight='weight')

def increase_matrix(matrix):
    bigger_matrix = []
    matrix_len = len(matrix)
    for row in matrix:
        tmp_row = []
        for col in row:
            tmp_row.append(int(col))
        for i in range(1, 5):
            new_tmp_row = []
            for k in range((i - 1) * matrix_len, i * matrix_len):
                el = tmp_row[k]
                num = (int(el) + 1) if (int(el) < 9) else 1
                new_tmp_row.append(num)
            tmp_row += new_tmp_row
        bigger_matrix.append(tmp_row)
    for row in range(matrix_len, 5 * matrix_len):
        new_row = []
        for col in range(0, 5 * matrix_len):
            el = bigger_matrix[row - matrix_len][col] + 1
            if el > 9:
                el = 1
            new_row.append(el)
        bigger_matrix.append(new_row)
    # print(bigger_matrix)
    return bigger_matrix

def part2(matrix):
    bigger_matrix = increase_matrix(matrix)
    return part1(bigger_matrix)

if __name__ == '__main__':
    rows = get_all_input_rows('day15.txt')
    matrix = []
    for row in rows:
        tmp_row = []
        for el in row:
            tmp_row.append(int(el))
        matrix.append(tmp_row)
    print(f'Part 1: {part1(matrix)}')
    print(f'Part 2: {part2(matrix)}')
