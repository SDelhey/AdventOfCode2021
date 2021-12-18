filename = 'data.txt'


class Point:
    def __init__(self, point_as_str: str):
        self.x = int(point_as_str.split(',')[0])
        self.y = int(point_as_str.split(',')[1])

    def __str__(self):
        return f"{self.x},{self.y}"


def add_horizontal_or_vertical_line(output: dict, p1: Point, p2: Point):
    start = min(p1.x, p2.x) if p1.x != p2.x else min(p1.y, p2.y)
    end = max(p1.x, p2.x) if p1.x != p2.x else max(p1.y, p2.y)

    for i in range(start, end + 1):
        position = f"{p1.x if p1.x == p2.x else i},{p1.y if p1.y == p2.y else i}"

        if position in output:
            output[position] += 1
        else:
            output[position] = 1


def add_diagonal_lines(output: dict, p1: Point, p2: Point):
    length = abs(p1.x - p2.x) + 1
    for i in range(length):
        if p1.x < p2.x:
            x_pos = p1.x + i
        else:
            x_pos = p1.x - i

        if p1.y < p2.y:
            y_pos = p1.y + i
        else:
            y_pos = p1.y - i

        position = f"{x_pos},{y_pos}"
        if position in output:
            output[position] += 1
        else:
            output[position] = 1


with open(filename) as file:
    result = {}

    for line in file:
        p1 = Point(line.split(' ')[0])
        p2 = Point(line.split(' ')[2])

        if p1.x == p2.x or p1.y == p2.y:
            add_horizontal_or_vertical_line(result, p1, p2)

        else:
            add_diagonal_lines(result, p1, p2)

    final = [k for k, v in result.items() if v >= 2]
    print(len(final))
