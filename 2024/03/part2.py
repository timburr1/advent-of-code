import re

def calculate_value(string):
    vals = string.replace('mul(', '').replace(')', '').split(',')
    product = int(vals[0]) * int(vals[1])
    return product

def evaluate(input):
    sections = input.split('do()') 
    print(str(len(sections)))

    total = 0

    for s in sections:
        #print(s)

        do = s.split('don\'t()')[0]
        for mul in re.findall('mul\([0-9]+,[0-9]+\)', do):
            total += calculate_value(mul)

    return total

with open('concat.txt') as fp:
    sum = 0
    for line in fp:
        #print(evaluate(line))
        sum += evaluate(line)
    print(str(sum))
