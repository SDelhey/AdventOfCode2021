filename = 'data.txt'


class Point:
    def __init__(self, point_as_str: str):
        self.x = int(point_as_str.split(',')[0])
        self.y = int(point_as_str.split(',')[1])

    def distance_to(self, other_point: "Point"):
        pass

    def __str__(self):
        return f"{self.x},{self.y}"


# def add_vents_to_result(constant_axis: str, p1: Point, p2: Point):
#     const = p1.x if constant_axis is 'x' else p1.y
#     min =


with open(filename) as file:
    result = {}

    for line in file:
        p1 = Point(line.split(' ')[0])
        p2 = Point(line.split(' ')[2])

        if p1.x == p2.x:
            x = p1.x
            y1 = min(p1.y, p2.y)
            y2 = max(p1.y, p2.y)

            for i in range(y1, y2 + 1):
                position = f"{x},{i}"

                if position in result:
                    result[position] += 1
                else:
                    result[position] = 1
        elif p1.y == p2.y:
            y = p1.y
            x1 = min(p1.x, p2.x)
            x2 = max(p1.x, p2.x)

            for i in range(x1, x2 + 1):
                position = f"{i},{y}"

                if position in result:
                    result[position] += 1
                else:
                    result[position] = 1

    print(result)
    final = [k for k, v in result.items() if v >= 2]
    print(len(final))
