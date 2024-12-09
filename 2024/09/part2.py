import sys

def expand(dm):
    result = []
    c = 0
    for i in range(0, len(dm), 2):
        file_len = int(dm[i])
        if i < len(dm) - 1:
            empty_len = int(dm[i+1])
        else:
            empty_len = 0

        for j in range(0, file_len):
            result.append(str(c))
        for k in range(0, empty_len):
            result.append('.')
        
        c += 1

    return result

def compress(dm):    
    i = 0
    j = len(dm)-1
    while i < j:
        if dm[i] != '.':
            i += 1 
            continue
        while dm[j] == '.':
            j -= 1
        
        dm = dm[:i] + [dm[j]] + dm[i+1:j] + ['.'] + dm[j+1:]
        
    return dm

def checksum(dm):
    sum = 0

    for i in range(0, len(dm)):
        if dm[i] == '.':
            continue
        else:
            sum += i * int(dm[i])

    return sum

with open('2024/09/input.txt') as fp:
    for line in fp:
        e = expand('2333133121414131402') # checksum = 2858
        # e = expand('233313312141413140211') 
        # e = expand(line.replace('\n', ''))
        print(e)
        print('\n--------------------\n')
        c = compress(e)
        print(c)
        print(str(checksum(c)))

        # print(str(checksum(compress(expand(line.replace('\n', ''))))))
