filename = 'data.txt'


def part1():
    with open(filename) as file:
        lines = file.readlines()
        all_outputs = [line.split(' | ')[1] for line in lines]
        unique_pattern_length = [2, 4, 3, 7]
        result = [output for outputs in all_outputs for output in outputs.split(' ') if len(output.rstrip('\n')) in unique_pattern_length]
        print(len(result))


def find_by_unique_amount_of_characters(patterns: list[str], amount: int):
    return [pattern for pattern in patterns if len(pattern) == amount][0]


def find_three(patterns: list[str], seven: str):
    return [pattern for pattern in patterns if len(pattern) == 5 and all(c in pattern for c in seven)][0]


def find_nine(patterns: list[str], four):
    return [pattern for pattern in patterns if len(pattern) == 6 and all(c in pattern for c in four)][0]


def find_six(patterns: list[str], one, nine):
    return [pattern for pattern in patterns if len(pattern) == 6 and not all(c in pattern for c in one) and pattern != nine][0]


def find_zero(patterns: list[str], nine, six):
    return [pattern for pattern in patterns if len(pattern) == 6 and pattern != nine and pattern != six][0]


def find_five(patterns: list[str], three, six):
    return [pattern for pattern in patterns if len(pattern) == 5 and pattern != three and all(c in six for c in pattern)][0]


def find_two(patterns: list[str], three, five, six):
    return [pattern for pattern in patterns if len(pattern) == 5 and pattern != three and pattern != five and pattern != six][0]


def part2():
    with open(filename) as file:
        lines = file.readlines()
        inputs = [line.split(' | ') for line in lines]
        result = []

        for input in inputs:
            # Same as part 1
            one = find_by_unique_amount_of_characters(input[0].split(' '), 2)
            four = find_by_unique_amount_of_characters(input[0].split(' '), 4)
            seven = find_by_unique_amount_of_characters(input[0].split(' '), 3)
            eight = find_by_unique_amount_of_characters(input[0].split(' '), 7)

            three = find_three(input[0].split(' '), seven)
            nine = find_nine(input[0].split(' '), four)
            six = find_six(input[0].split(' '), one, nine)
            zero = find_zero(input[0].split(' '), nine, six)
            five = find_five(input[0].split(' '), three, six)
            two = find_two(input[0].split(' '), three, five, six)

            enc = {
                ''.join(sorted(zero)): 0,
                ''.join(sorted(one)): 1,
                ''.join(sorted(two)): 2,
                ''.join(sorted(three)): 3,
                ''.join(sorted(four)): 4,
                ''.join(sorted(five)): 5,
                ''.join(sorted(six)): 6,
                ''.join(sorted(seven)): 7,
                ''.join(sorted(eight)): 8,
                ''.join(sorted(nine)): 9
            }

            outputs = input[1].strip().split(' ')
            number = ''
            for output in outputs:
                number += str(enc[''.join(sorted(output))])

            result.append(int(number))

        print(sum(result))


if __name__ == '__main__':
    part1()
    part2()