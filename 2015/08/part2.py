import re

def encode(string):
    string = string.replace('\\', '\\\\')
    string = string.replace('"', '\\\"')
    print('\"' + string + '\"')
    return '\"' + string + '\"'

total_len = 0
encoded_len = 0
with open('2015/08/input.txt') as fp:
    for line in fp:
        line = line.strip()
        total_len += len(line)
        # print(line.encode(encoding="ascii"))
        encoded_len += len(encode(line))

# print(str(total_len))
# print(str(memory_len))
print(str(encoded_len - total_len))
