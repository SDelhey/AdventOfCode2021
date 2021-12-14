filename = 'data.txt'

def  decimalFromReverseBinary(number_as_string):
    length = len(number_as_string)

    reversed_number = number_as_string[::-1]
    decimal_number = 0
    for i in range(length):
        decimal_number += int(reversed_number[i]) * pow(2, i)

    return decimal_number

# Part 1
with open(filename) as file:
    lines  = file.readlines()
    length = len(lines[0])
    most_common = ''
    least_common = ''

    for i in range(length - 1):
        digits = [line[i] for line in lines]
        most_common += max(set(digits), key=digits.count)
        least_common += min(set(digits), key=digits.count)


    gamma_rate = decimalFromReverseBinary(most_common)
    epsilon_rate = decimalFromReverseBinary(least_common)

    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)

# Part 2
from collections import Counter
def getMostCommon(list):
    dict = Counter(list)

    if dict['1'] >= dict['0']:
        return 1
    elif dict['0'] > dict['1']:
        return 0

def getLeastCommon(list):
    dict = Counter(list)

    if dict['1'] < dict['0']:
        return 1
    elif dict['0'] <= dict['1']:
        return 0

with open(filename) as file:
    files = file.readlines()
    length = len(files[0])

    files_most_common = files.copy()
    files_least_common = files.copy()

    for i in range(length - 1):
        digits_most_common = [line[i] for line in files_most_common]
        digits_least_common = [line[i] for line in files_least_common]
        most_common = getMostCommon(digits_most_common)
        least_common = getLeastCommon(digits_least_common)

        if len(files_most_common) > 1:
            files_most_common = [line for line in files_most_common if int(line[i]) == most_common]

        if len(files_least_common) > 1:
            files_least_common = [line for line in files_least_common if int(line[i]) == least_common]

    oxygen_score = decimalFromReverseBinary(str(int(files_most_common[0])))
    c02_score = decimalFromReverseBinary(str(int(files_least_common[0])))
    life_support_score = oxygen_score * c02_score
    print(life_support_score)
