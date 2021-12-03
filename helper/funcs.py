import os, sys

def get_all_input_rows(filename):
    dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dir, f'..\input\{filename}')
    file = open(filepath, 'r')
    rows = file.read().split('\n')
    return rows

def bin_to_decimal(bin_str):
    n = len(bin_str)
    decimal = 0
    for bit in bin_str:
        if bit == '1':
            decimal += pow(2, n - 1)
        n -= 1
    return decimal