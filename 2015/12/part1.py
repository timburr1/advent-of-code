import re

def sum(input):
    sum = 0
    for num in re.findall('-?[0-9]+', input):
        sum += int(num)

    return sum 

with open('2015/12/input.txt') as fp:
    for line in fp:
        print(sum(line.strip()))
