filename = 'data.txt'

# Part 1
with open(filename) as file:
    prev = None
    counter = 0
    for line in file:
        line = int(line)

        if prev is not None and line > prev:
            counter += 1

        prev = line

    print(counter)


# Part 2
with open(filename) as file:
    size = 3
    prev = None
    counter = 0

    lines = file.readlines()
    lines = [int(line) for line in lines]

    for i in range(len(lines) - size + 1):
        current_lines = lines[i:i + size]
        current_lines_sum = sum(current_lines)

        if prev is not None and current_lines_sum > prev:
            counter += 1

        prev = current_lines_sum

    print(counter)
