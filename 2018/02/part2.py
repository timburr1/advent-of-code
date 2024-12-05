
def compare(id1, id2):
    diff_count = 0

    for n in range(0, len(id1)):
        if id1[n] != id2[n]:
            diff_count += 1

    return diff_count == 1

def diff(id1, id2):
    result = ''

    for n in range(0, len(id1)):
        if id1[n] == id2[n]:
            result += id1[n]

    return result

ids = []

with open('2018/02/input.txt') as fp:
    for line in fp:
        ids.append(line.replace('\n', ''))

for i in range(0, len(ids)):
    for j in range(i+1, len(ids)):
        if compare(ids[i], ids[j]):
            print(diff(ids[i], ids[j]))
            break
