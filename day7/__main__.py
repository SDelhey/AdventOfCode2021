from statistics import median_low

filename = 'data.txt'


def part_1():
    with open(filename) as file:
        positions = list(map(int, file.read().split(',')))
        median = median_low(positions)
        costs = 0

        for position in positions:
            costs += abs(median - position)

        print(costs)


def part_2():
    with open(filename) as file:
        positions = list(map(int, file.read().split(',')))
        costs = None

        values_to_consider = [value for value in range(min(positions), max(positions))]
        for value in values_to_consider:
            current_costs = 0

            for position in positions:
                old_costs = abs(value - position)
                current_costs += sum([idx for idx in range(1, old_costs + 1)])

            if costs is None or current_costs < costs:
                costs = current_costs

        print(costs)


if __name__ == '__main__':
    part_1()
    part_2()
