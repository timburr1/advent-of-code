
def is_anagram(str1, str2):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for l in letters:
        if str1.count(l) != str2.count(l):
            return False

    return True

def includes_anagram(target, vals):
    for v in vals:
        if len(target) != len(v):
            continue
        if is_anagram(target, v):
            return True     
    return False

def test(tokens):
    tested = set()

    for i in range(0, len(tokens)):
        if tokens[i] in tested or includes_anagram(tokens[i], tokens[:i] + tokens[i+1:]):
            return False
        else:
            tested.add(tokens[i])

    return True

count = 0
with open('2017/04/input.txt') as fp:
    for line in fp:
        line = line.replace('\n', '')
        if test(line.split(' ')):
            # print(line)
            count += 1

print(str(count))
        