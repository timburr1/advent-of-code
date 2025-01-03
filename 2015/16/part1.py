
clues = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

def match(input):
    global clues

    s = input.split(' ')
    # print(str(s))
    for i in range(2, len(s), 2):
        k = s[i].replace(':', '')
        v = int(s[i+1].replace(',', ''))
        if clues[k] != v:
            return False
    return True

with open('2015/16/input.txt') as fp:    
    for line in fp:
        if match(line.strip()):
            print(line)
            break
        