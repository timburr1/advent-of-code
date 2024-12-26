
def rotate(string, val):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    result = ''
    for s in string:
        result += letters[(letters.find(s) + val) % 26]

    return result

def decrypt(input):
    i = input.split('[')
    j = i[0].split('-')

    id = int(j[len(j) - 1])

    r = ''
    for k in range(len(j) - 1):
        r += rotate(j[k], id) + ' '
    return str(id) + ': ' + r

with open('2016/04/input.txt') as fp:
    for line in fp:
        print(decrypt(line.strip()))
