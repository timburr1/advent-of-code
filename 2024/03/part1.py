import re

def calculate_value(string):
    vals = string.replace('mul(', '').replace(')', '').split(',')
    product = int(vals[0]) * int(vals[1])
    #print(str(product))
    return product

def evaluate(input):
    total = 0

    #print(re.findall('mul\([0-9]+,[0-9]+\)', input))

    for mul in re.findall('mul\([0-9]+,[0-9]+\)', input):
        total += calculate_value(mul)

    return total

with open('2024/03/input.txt') as fp:
    sum = 0
    for line in fp:
        #print(evaluate(line))
        sum += evaluate(line)
    print(str(sum))
