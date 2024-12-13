import re

def check(input):
    substrings = re.split('', input)
    for s in substrings:
        if check_sub(s):
            return True
    return False

def check_sub(substring):
    if len(substring) < 4:
        return False
    for i in range(0, len(substring)-4):
        if substring[i] == substring[i+]

c = 0
with open("2016/07/test.txt") as fp:
    for line in fp:
        if check(line.strip()):
            c += 1
print(c)
