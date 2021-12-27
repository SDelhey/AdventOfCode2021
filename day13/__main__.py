import numpy as np
filename = 'data.txt'


def apply_x_fold(field, offset):
    for i in range(len(field)):
        for j in range(len(field[i])):

            if j <= offset:
                continue

            dist = j - offset
            field[i][j - 2*dist] = field[i][j - 2*dist] | field[i][j]

    return [row[0:offset] for row in field]


def apply_y_fold(field, offset):
    for i in range(len(field)):
        for j in range(len(field[i])):

            if i <= offset:
                continue

            dist = i - offset
            field[i - 2*dist][j] = field[i - 2*dist][j] | field[i][j]

    return field[0:offset]


def print_grid(field):
    for row in field:
        print("".join("#" if val > 0 else ' ' for val in row))


def part1(all_folds: bool = False):
    with open(filename) as file:
        lines = file.readlines()
        dots = [[int(val) for val in line.rstrip().split(',')] for line in lines if ',' in line]
        folds = [line.rstrip() for line in lines if ',' not in line and len(line.rstrip()) > 0]

        max_x = max([item[0] for item in dots]) + 1
        max_y = max([item[1] for item in dots]) + 1

        field = np.zeros((max_y, max_x), dtype=int).tolist()

        for dot in dots:
            field[dot[1]][dot[0]] = 1

        if not all_folds:
            for i in range(1):
                offset = int(folds[i].split(' ')[-1].split('=')[-1])
                if 'x' in folds[i]:
                    field = apply_x_fold(field, offset)
                else:
                    field = apply_y_fold(field, offset)

        else:
            for item in folds:
                offset = int(item.split(' ')[-1].split('=')[-1])
                if 'x' in item:
                    field = apply_x_fold(field, offset)
                else:
                    field = apply_y_fold(field, offset)

        field = np.array(field)
        print(sum(1 for row in field for val in row if val > 0))

        if all_folds:
            print_grid(field)


def part2():
    part1(True)


if __name__ == '__main__':
    part1()
    part2()
