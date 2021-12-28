from collections import defaultdict
from typing import List

filename = 'data.txt'


def read_insertion_rules(lines: List[str]):
    rules = {}

    for line in lines:
        rule = line.rstrip().split(' -> ')
        rules[rule[0]] = rule[1]

    return rules


def apply_rules(template: str, rules: dict):
    template_copy = template

    for i in range(len(template) - 1):
        insertion = rules[template[i]+template[i+1]]
        template_copy = template_copy[0:2*i+1] + insertion + template_copy[2*i+1:]

    return template_copy


def template_to_tuple_dict(template: str):
    return  {''.join(pair): 1 for pair in zip(template[:-1], template[1:])}


def apply_rules_fast(tuple_dict: dict, rules: dict):
    updated_tuple_dict = defaultdict(int)

    for poly, count in tuple_dict.items():
        tuple_dict[poly] -= count
        updated_tuple_dict[poly[0] + rules[poly]] += count
        updated_tuple_dict[rules[poly] + poly[1]] += count

    return updated_tuple_dict


def part1(steps = 10):
    with open(filename) as file:
        lines = file.readlines()
        template = lines[0].rstrip()
        insertion_rules = read_insertion_rules(lines[2:])

        for step in range(steps):
            template = apply_rules(template, insertion_rules)

        occurrences = [template.count(character) for character in set(template)]
        print(occurrences)
        print(max(occurrences) - min(occurrences))


def part2(steps=10):
    with open(filename) as file:
        lines = file.readlines()
        template = lines[0].rstrip()
        insertion_rules = read_insertion_rules(lines[2:])

        template = template_to_tuple_dict(template)
        for step in range(steps):
            tmp_template = apply_rules_fast(template, insertion_rules)

            for k, v in tmp_template.items():
                template[k] = v

        counts = defaultdict(int)
        for pair, count in template.items():
            counts[pair[0]] += count

        counts[lines[0].rstrip()[-1]] += 1

        print(max(counts.values()) - min(counts.values()))

if __name__ == '__main__':
    part1()
    part2()
