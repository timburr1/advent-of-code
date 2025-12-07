
ranges = []
def add_range(input):
    return

def is_fresh(input):
    global ranges

    return False

count = 0

with open('2025/05/test.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        # print(line)
        if line.count('-') > 0:
            add_range(line)
        elif len(line) == 0:
            continue
        elif is_fresh(line):
            count += 1
        
print(str(count))