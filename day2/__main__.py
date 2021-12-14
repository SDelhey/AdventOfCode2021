
filepath = 'data.txt'
# Part 1
with open(filepath) as file:
    depth = 0
    position = 0

    for line in file:
        split_line = line.split(' ')
        direction = split_line[0]
        distance = int(split_line[1])

        if direction == 'forward':
            position += distance

        elif direction == 'down':
            depth += distance

        else:
            depth -= distance

    print(depth*position)


# Part 2
with open(filepath) as file:
    depth = 0
    position = 0
    aim = 0

    for line in file:
        split_line = line.split(' ')
        direction = split_line[0]
        distance = int(split_line[1])

        if direction == 'forward':
            position += distance
            depth += aim * distance

        elif direction == 'down':
            aim += distance

        else:
            aim -= distance

    print(depth*position)