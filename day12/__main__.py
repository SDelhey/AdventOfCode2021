from typing import List
filename = 'data.txt'


def get_possible_paths(lines: List[str], node: str):
    result = [elements[1] if elements[0] == node else elements[0] for elements in lines if node in elements]

    if 'start' in result:
        result.remove('start')
    return result


def visited_small_cave_twice(path: str):
    path = path.split(',')
    last_node = path[-1]

    if last_node.islower() and path.count(last_node) > 1:
        return True
    return False


def explore(lines: List[str], result: List, root='start', path='start'):
    if visited_small_cave_twice(path):
        return

    if root == 'end' or visited_small_cave_twice(path):
        result.append(path)
        return

    for pp in get_possible_paths(lines, root):
        explore(lines, result, pp, f"{path},{pp}")


def part1():
    with open(filename) as file:
        lines = [[element.rstrip() for element in line.split('-')] for line in file.readlines()]
        result = []
        explore(lines, result)
        print(len(result))


def visited_only_one_small_cave_at_most_twice(path: str):
    path = path.split(',')
    small_caves = list(set([cave for cave in path if cave.islower()]))

    # check if any small cave is visited more than twice
    small_caves_counter = [path.count(cave) for cave in small_caves]
    if any(val > 2 for val in small_caves_counter):
        return True

    # check if multiple caves are visited more than once
    if sum(1 for val in small_caves_counter if val > 1) > 1:
        return True

    return False


def explore_p2(lines: List[str], result: List, root='start', path='start'):
    if visited_only_one_small_cave_at_most_twice(path):
        return

    if root == 'end' or visited_only_one_small_cave_at_most_twice(path):
        result.append(path)
        return

    for pp in get_possible_paths(lines, root):
        explore_p2(lines, result, pp, f"{path},{pp}")


def part2():
    with open(filename) as file:
        lines = [[element.rstrip() for element in line.split('-')] for line in file.readlines()]
        result = []
        explore_p2(lines, result)
        print(len(result))


if __name__ == '__main__':
    part1()
    part2()
