import os, sys

def count_increasing(elements):
    counter = 0
    for i in range(len(elements) - 1):
        if int(elements[i]) < int(elements[i + 1]):
            counter += 1   
    return counter

def part1():
    dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dir, '..\input\day01.txt')
    file = open(filename, "r")
    input = file.read()
    # read every row of input file
    rows = input.split("\n")
    counter = count_increasing(rows)    
    print(f'counter = {counter}')
    file.close()

def part2():
    dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dir, '..\input\day01.txt')
    file = open(filename, "r")
    input = file.read()
    rows = input.split("\n")
    elements = []
    a_arr = []
    b_arr = []
    c_arr = []
    d_arr = []
    a_arr.append(int(rows[0]))
    a_arr.append(int(rows[1]))
    b_arr.append(int(rows[1]))
    a_arr.append(int(rows[2]))
    b_arr.append(int(rows[2]))
    c_arr.append(int(rows[2]))
    b_arr.append(int(rows[3]))
    c_arr.append(int(rows[3]))
    d_arr.append(int(rows[3]))
    for i in range(4, len(rows)):
        if len(a_arr) == 3:
            elements.append(sum(a_arr))
            a_arr = []
        if len(b_arr) == 3:
            elements.append(sum(b_arr))
            b_arr = []
        if len(c_arr) == 3:
            elements.append(sum(c_arr))
            c_arr = []
        if len(d_arr) == 3:
            elements.append(sum(d_arr))
            d_arr = []
        if i % 4 == 0 or i % 4 == 1 or i % 4 == 2:
            a_arr.append(int(rows[i]))
        if i % 4 == 1 or i % 4 == 2 or i % 4 == 3:
            b_arr.append(int(rows[i]))
        if i % 4 == 2 or i % 4 == 3 or i % 4 == 0:
            c_arr.append(int(rows[i]))
        if i % 4 == 3 or i % 4 == 0 or i % 4 == 1:
            d_arr.append(int(rows[i]))
    if len(a_arr) == 3:
        elements.append(sum(a_arr))
        a_arr = []
    if len(b_arr) == 3:
        elements.append(sum(b_arr))
        b_arr = []
    if len(c_arr) == 3:
        elements.append(sum(c_arr))
        c_arr = []
    if len(d_arr) == 3:
        elements.append(sum(d_arr))
        d_arr = []
    print(count_increasing(elements))
    file.close()
    
if __name__ == "__main__":
    # part1()
    part2()