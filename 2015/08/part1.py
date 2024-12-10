import re

total_len = 0
memory_len = 0
with open('2015/08/test.txt') as fp:
    for line in fp:
        line = line.strip()
        total_len += len(line)
        memory_len += len(eval(line))

# print(str(total_len))
# print(str(memory_len))
print(str(total_len - memory_len))
