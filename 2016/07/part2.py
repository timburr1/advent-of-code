import re

def check(s):
    if len(s) < 4:
        return False
    for i in range(0, len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False

lines = [re.split(r'\[([^\]]+)\]', line) for line in open('2016/07/input.txt')]
parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]
# print(sum(check(sn) and not(check(hn)) for sn, hn in parts))
print(sum(any(a == c and a != b and b+a+b in hn for a, b, c in zip(sn, sn[1:], sn[2:])) for sn, hn in parts))
