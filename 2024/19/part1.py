
patterns = []

def check_design(towel):
    global patterns

    

c = 0
with open('2024/19/test.txt') as fp:
    for line in fp:
        # print(line.strip())
        if line.count(',') > 0:
            patterns += line.strip().split(', ')
            print(str(patterns))
        elif line == '\n':
            continue
        else:
            if check_design(line.strip()):
                c += 1
print(c)