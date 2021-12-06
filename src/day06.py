import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def part1(days, lanternfishes):
    for day in range(0, days):
        new_lanternfishes = []
        for i in range(0, len(lanternfishes)):
            if lanternfishes[i] == 0:
                lanternfishes[i] = 7
                new_lanternfishes.append(8)
            lanternfishes[i] -= 1
        for new_lanternfish in new_lanternfishes:
            lanternfishes.append(new_lanternfish)
    return len(lanternfishes)

# more optimal solution
def part2(days, lanternfishes):
    for day in range(0, days):
        l0 = lanternfishes[0]
        lanternfishes[0] = lanternfishes[1]
        lanternfishes[1] = lanternfishes[2]
        lanternfishes[2] = lanternfishes[3]
        lanternfishes[3] = lanternfishes[4]
        lanternfishes[4] = lanternfishes[5]
        lanternfishes[5] = lanternfishes[6]
        lanternfishes[6] = lanternfishes[7] + l0
        lanternfishes[7] = lanternfishes[8]
        lanternfishes[8] = l0
    return sum(lanternfishes)

if __name__ == '__main__':
    rows = get_all_input_rows('day06.txt')[0]
    lanternfishes = [int(el) for el in rows.split(',')]
    lanternfishes_arr = [0] * 9
    for lanternfish in lanternfishes:
        lanternfishes_arr[lanternfish] += 1
    print(f'Part 1: {part2(80, list(lanternfishes_arr))}')
    print(f'Part 2: {part2(256, list(lanternfishes_arr))}')