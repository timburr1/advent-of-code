
def match(name, checksum):
    letters = dict()

    for i in range(len(name)):
        if letters.get(name[i]) == None:
            letters[name[i]] = 1
        else:
            letters[name[i]] += 1

    tmp = sorted(letters.items(), key=lambda x:x[0])
    tmp = sorted(tmp, key=lambda x:x[1], reverse=True)

    # print(str(tmp))
    for i in range(len(checksum)):
        if tmp[i][0] != checksum[i]:
            return False
    return True

def check_line(input):
    parts = input.split('-')
    name = ''
    for i in range(len(parts) - 1):
        name += parts[i]
    end = parts[len(parts)-1].split('[')
    sector_id = int(end[0])
    checksum = end[1].replace(']', '')

    if match(name, checksum):
        return sector_id
    return 0

sum = 0
with open('2016/04/input.txt') as fp:
    for line in fp:
        sum += check_line(line.strip())
print(sum)
