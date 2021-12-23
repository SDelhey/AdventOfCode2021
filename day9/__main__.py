import functools
from typing import List

filename = 'data.txt'


def check_adjacent_numbers(all_numbers: List[List[int]], i: int, j: int) -> bool:
    current_value = all_numbers[i][j]

    if len(all_numbers) >= i + 2 and all_numbers[i + 1][j] <= current_value:
        return False

    if i > 0 and all_numbers[i - 1][j] <= current_value:
        return False

    if len(all_numbers[i]) >= j + 2 and all_numbers[i][j + 1] <= current_value:
        return False

    if j > 0 and all_numbers[i][j - 1] <= current_value:
        return False
    return True


def calculate_risk_level(low_points: List[int]) -> int:
    return sum(low_points) + len(low_points)


def part1():
    with open(filename) as file:
        lines = [[int(number) for number in line.rstrip()] for line in file.readlines()]
        low_points = [lines[i][j] for i in range(len(lines)) for j in range(len(lines[0])) if check_adjacent_numbers(lines, i, j)]
        risk_level = calculate_risk_level(low_points)
        print(risk_level)


def explore_for_basis(all_numbers):
    low_points = [(i, j) for i in range(len(all_numbers)) for j in range(len(all_numbers[0])) if check_adjacent_numbers(all_numbers, i, j)]
    results = []

    for low_point in low_points:
        current_value = all_numbers[low_point[0]][low_point[1]]
        already_visited_points = {low_point}

        __explore_for_basis(all_numbers, current_value, low_point[0] + 1, low_point[1], already_visited_points)
        __explore_for_basis(all_numbers, current_value, low_point[0] - 1, low_point[1], already_visited_points)
        __explore_for_basis(all_numbers, current_value, low_point[0], low_point[1] + 1, already_visited_points)
        __explore_for_basis(all_numbers, current_value, low_point[0], low_point[1] - 1, already_visited_points)

        results.append(len(already_visited_points))

    return functools.reduce(lambda x, y: x * y, sorted(results)[-3:])


def __is_part_of_basin(old_value, current_value):
    if current_value == 9:
        return False

    if current_value > old_value:
        return True

    return False


def index_out_of_bounds(all_numbers, i, j):
    if i < 0 or j < 0 or i + 1 > len(all_numbers) or j + 1 > len(all_numbers[i]):
        return True
    return False


def __explore_for_basis(all_numbers, old_value, i, j, already_visited):
    if index_out_of_bounds(all_numbers, i, j) or not __is_part_of_basin(old_value, all_numbers[i][j]) or (i, j) in already_visited:
        return

    current_value = all_numbers[i][j]
    already_visited.add((i, j))

    __explore_for_basis(all_numbers, current_value, i + 1, j, already_visited)
    __explore_for_basis(all_numbers, current_value, i - 1, j, already_visited)
    __explore_for_basis(all_numbers, current_value, i, j + 1, already_visited)
    __explore_for_basis(all_numbers, current_value, i, j - 1, already_visited)

    return


def part2():
    with open(filename) as file:
        lines = [[int(number) for number in line.rstrip()] for line in file.readlines()]
        basins_score = explore_for_basis(lines)
        print(basins_score)


if __name__ == '__main__':
    part1()
    part2()
