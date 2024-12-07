
def test(tokens):
    tested = set()

    for t in tokens:
        if t in tested:
            return False
        else:
            tested.add(t)

    return True

count = 0
with open('2017/04/input.txt') as fp:
    for line in fp:
        if test(line.replace('\n', '').split(' ')):
            count += 1

print(str(count))
        