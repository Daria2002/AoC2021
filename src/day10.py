import os, sys
from day09 import part1
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

close = [')', ']', '}', '>']
open = ['(', '[', '{', '<']
price = [3, 57, 1197, 25137]
price2 = [1, 2, 3, 4]

def part1(rows):
    points = 0
    for row in rows:
        tmp = []
        for el in row:
            if el in close:
                if len(tmp) > 0 and tmp[-1] == open[close.index(el)]:
                    tmp.pop()
                else:
                    points += price[close.index(el)]
                    break
            else:
                tmp.append(el)
    return points
        
def part2(rows):
    points_arr = []
    for row in rows:
        tmp = []
        for el in row:
            if el in close:
                if len(tmp) > 0 and tmp[-1] == open[close.index(el)]:
                    tmp.pop()
                else:
                    tmp = []
                    break
            else:
                tmp.append(el)
        points = 0
        for i in range(len(tmp) - 1, -1, -1):
            el = tmp[i]
            points *= 5
            points += price2[open.index(el)]
        if points > 0:
            points_arr.append(points)
    points_arr = sorted(points_arr)
    return points_arr[len(points_arr) // 2]

if __name__ == "__main__":
    rows = get_all_input_rows('day10.txt')
    print(f'Part1 = {part1(rows)}')
    print(f'Part2 = {part2(rows)}')