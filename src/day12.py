import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.funcs import *

def small_cave_visited_more_than_once(paths):
    count_dict = {}
    for path in paths:
        if path.isupper():
            continue
        if path not in count_dict:
            count_dict[path] = 0
        count_dict[path] += 1
        if count_dict[path] > 1:
            return True
    return False

def part1(paths, curr_position, curr_path, visited):
    if curr_position == 'end':
        if small_cave_visited_more_than_once(curr_path):
            return 0
        return 1
    count = 0
    for potential_path in paths[curr_position]:
        if (potential_path not in paths and potential_path != "end") or (visited[potential_path] and potential_path.islower()):
            continue
        tmp_path = list(curr_path)
        tmp_path.append(potential_path)
        visited[potential_path] = True
        count += part1(paths, potential_path, tmp_path, visited)
        visited[potential_path] = False
    return count

def transform_input(rows):
    data = {}
    visited = {}
    for row in rows:
        start, end = row.split('-')
        if start not in data:
            data[start] = []
        data[start].append(end)
        if end != 'end' and start != 'start':
            if end not in data:
                data[end] = []
            data[end].append(start)
        visited[end] = False if end != 'start' else True
        visited[start] = False if start != 'start' else True
    return data, visited

if __name__ == '__main__':
    rows = get_all_input_rows('day12.txt')
    paths, visited = transform_input(rows)
    print(f'part 1: {part1(paths, "start", ["start"], visited)}')