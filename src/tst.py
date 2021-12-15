from functools import reduce

arr = [1, 2, 3, 4, 5]

def my_add(a, b):
    print(f'a: {a}, b: {b}')
    return a + b

print(f'arr = {reduce(my_add, arr)}')