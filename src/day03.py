import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
from helper.funcs import * 

def part1(rows):
    n = len(rows[0])
    count_bits = [0] * n
    for row in rows:
        for i, bit in enumerate(row):
            if bit == '1':
                count_bits[i] += 1
            elif bit == '0':
                count_bits[i] -= 1
            else:
                print(f'somethings wrong')
    gamma = 0
    epsilon = 0
    for bit in count_bits:
        if bit > 0: # most common bit is 1
            gamma += pow(2, n - 1)
        elif bit < 0: # most common bit is 0
            epsilon += pow(2, n - 1)
        else: # there is the same number of 0 and 1 bits
            print(f'there is the same number of 0 and 1 bits')
        n -= 1
    return gamma * epsilon

def part2(rows):
    rows_orig = list(rows)
    n = len(rows[0])
    for i in range(n):
        bit1 = []
        bit0 = []
        print(f'rows = {rows}')
        count_bits = 0
        for row in rows:
            if row[i] == '1':
                bit1.append(row)
                count_bits += 1
            elif row[i] == '0':
                bit0.append(row)
                count_bits -= 1
        if count_bits >= 0:
            rows = bit1
        else:
            rows = bit0
        if len(rows) == 1:
            oxygen_generator_rating = rows[0]
    rows = rows_orig
    n = len(rows[0])
    for i in range(n):
        bit1 = []
        bit0 = []
        print(f'rows = {rows}')
        count_bits = 0
        for row in rows:
            if row[i] == '1':
                bit1.append(row)
                count_bits += 1
            elif row[i] == '0':
                bit0.append(row)
                count_bits -= 1
        if count_bits >= 0:
            rows = bit0
        else:
            rows = bit1
        if len(rows) == 1:
            c02_scrubber_rating = rows[0]

    return bin_to_decimal(oxygen_generator_rating) * bin_to_decimal(c02_scrubber_rating)

if __name__ == '__main__':
    rows = get_all_input_rows('day03.txt')
    print(f'part1 = {part1(rows)}')
    print(f'part2 = {part2(rows)}')