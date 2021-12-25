from typing import List, Tuple
filename = 'data.txt'


def get_adjacent_horizontal(lines: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    adjacent = []

    # left adjacent
    if j > 0:
        adjacent.append((i, j - 1))

    # right adjacent
    if j < len(lines[i]) - 1:
        adjacent.append((i, j + 1))

    return adjacent


def get_adjacent_vertical(lines: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    adjacent = []

    # top adjacent
    if i > 0:
        adjacent.append((i - 1, j))

    # bottom adjacent
    if i < len(lines) - 1:
        adjacent.append((i + 1, j))

    return adjacent


def get_adjacent_diagonal(lines: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    adjacent = []

    # top-left adjacent
    if j > 0 and i > 0:
        adjacent.append((i - 1, j - 1))

    # top-right adjacent
    if j < len(lines[i]) - 1 and i > 0:
        adjacent.append((i - 1, j + 1))

    # bottom-left adjacent
    if j > 0 and i < len(lines) - 1:
        adjacent.append((i + 1, j - 1))

    # bottom-right adjacent
    if j < len(lines[i]) - 1 and i < len(lines) - 1:
        adjacent.append((i + 1, j + 1))

    return adjacent


def get_adjacent(lines: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    adjacent = []

    adjacent += get_adjacent_horizontal(lines, i, j)
    adjacent += get_adjacent_vertical(lines, i, j)
    adjacent += get_adjacent_diagonal(lines, i, j)

    return adjacent


def get_over_9(lines: List[List[int]], already_flashed: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] > 9 and (i, j) not in already_flashed]


def all_flashing(lines: List[List[int]]) -> bool:
    flattened_lines = [lines[i][j] for i in range(len(lines)) for j in range(len(lines[0]))]
    return all(val > 9 for val in flattened_lines)


def part1(steps: int = 100) -> None:
    with open(filename) as file:
        lines = [[int(number) for number in line.rstrip()] for line in file.readlines()]
        flashes = 0

        for i in range(steps):
            # Increase by 1
            lines = [[number + 1 for number in line] for line in lines]
            items_that_have_been_over_9 = []

            while True:
                over_9 = get_over_9(lines, items_that_have_been_over_9)

                for item in over_9:
                    adjacent = get_adjacent(lines, item[0], item[1])

                    for adj in adjacent:
                        lines[adj[0]][adj[1]] += 1

                items_that_have_been_over_9 += over_9
                new_over_9 = get_over_9(lines, items_that_have_been_over_9)
                if len(new_over_9) == 0:
                    flashes += len(items_that_have_been_over_9)
                    break

            lines = [[number if number <= 9 else 0 for number in line] for line in lines]

        print(flashes)


def part2(steps=99999) -> None:
    with open(filename) as file:
        lines = [[int(number) for number in line.rstrip()] for line in file.readlines()]
        flashes = 0

        for i in range(steps):
            # Increase by 1
            lines = [[number + 1 for number in line] for line in lines]
            items_that_have_been_over_9 = []

            while True:
                over_9 = get_over_9(lines, items_that_have_been_over_9)

                for item in over_9:
                    adjacent = get_adjacent(lines, item[0], item[1])

                    for adj in adjacent:
                        lines[adj[0]][adj[1]] += 1

                items_that_have_been_over_9 += over_9
                new_over_9 = get_over_9(lines, items_that_have_been_over_9)
                if len(new_over_9) == 0:
                    flashes += len(items_that_have_been_over_9)
                    break

            if all_flashing(lines):
                print(f"Iteration: {i + 1}")
                break

            lines = [[number if number <= 9 else 0 for number in line] for line in lines]

        print(flashes)


if __name__ == '__main__':
    part1()
    part2()
