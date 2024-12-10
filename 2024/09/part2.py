import sys

def expand(dm):
    free_blocks = []
    file_blocks = []

    for i in range(0, len(dm)):
        if i % 2 == 0:
            file_blocks.append(int(dm[i]))
        else:
            free_blocks.append(int(dm[i]))

    blocks = []
    for i in range(len(file_blocks)):
        blocks.append([str(i)] * file_blocks[i])
        if i < len(free_blocks):
            blocks.append(['.'] * free_blocks[i])
    return blocks

def compress(blocks):    
    for file_index in range(len(blocks)-1, -1, -1):
        file_block = blocks[file_index]

        if all(c == '.' for c in file_block):
            continue
        file_len = len(file_block)

        for i in range(0, file_index):
            if '.' in blocks[i] and len(blocks[i]) >= file_len:
                free_len = len(blocks[i])
                blocks[i] = file_block
                blocks[file_index] = ['.'] * file_len

                remainder = free_len - file_len
                if remainder > 0:
                    blocks.insert(i+1, ['.'] * remainder)
                break
            
    expanded_blocks = []
    for b in blocks:
        expanded_blocks.extend(b)
    return expanded_blocks

def checksum(blocks):
    sum = 0

    for i, b in enumerate(blocks):
        if b == '.':
            continue
        else:
            sum += i * int(b)

    return sum

with open('2024/09/input.txt') as fp:
    for line in fp:
        print(str(checksum(compress(expand(line.replace('\n', ''))))))
