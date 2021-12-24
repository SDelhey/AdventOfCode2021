from statistics import median

filename = 'data.txt'


def score_for_incorrect_character(character: str) -> int:
    if character == ')':
        return 3

    if character == ']':
        return 57

    if character == '}':
        return 1197

    if character == '>':
        return 25137

    raise Exception('Invalid Character')


def get_correct_closing_character(last_opening_character: str) -> str:
    if last_opening_character == '(':
        return ')'

    if last_opening_character == '[':
        return ']'

    if last_opening_character == '{':
        return '}'

    if last_opening_character == '<':
        return '>'

    raise Exception('Invalid Character')


def is_opening_character(character: str) -> bool:
    if character == '(' or character == '[' or character == '{' or character == '<':
        return True
    else:
        return False


def part1() -> None:
    with open(filename) as file:
        lines = [line.rstrip() for line in file.readlines()]
        results = 0

        for line in lines:
            opening_characters = []

            for character in line:
                if is_opening_character(character):
                    opening_characters.append(character)

                elif get_correct_closing_character(opening_characters.pop()) != character:
                    results += score_for_incorrect_character(character)
                    break

        print(results)


def score_for_missing_character(character: str) -> int:
    if character == ')':
        return 1

    if character == ']':
        return 2

    if character == '}':
        return 3

    if character == '>':
        return 4

    raise Exception('Invalid Character')


def line_is_corrupted(line: str) -> bool:
    opening_characters = []

    for character in line:
        if is_opening_character(character):
            opening_characters.append(character)

        elif get_correct_closing_character(opening_characters.pop()) != character:
            return True

    return False


def part2() -> None:
    with open(filename) as file:
        lines = [line.rstrip() for line in file.readlines()]
        incomplete_lines = [line for line in lines if not line_is_corrupted(line)]
        results = []

        for line in incomplete_lines:
            opening_characters = []

            for character in line:
                if is_opening_character(character):
                    opening_characters.append(character)

                else:
                    opening_characters.pop()

            tmp_result = 0
            for character in reversed(opening_characters):
                closing_character = get_correct_closing_character(character)
                tmp_result = tmp_result * 5 + score_for_missing_character(closing_character)
            results.append(tmp_result)

        print(median(sorted(results)))


if __name__ == '__main__':
    part1()
    part2()
