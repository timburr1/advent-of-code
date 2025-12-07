
ranges = []
def add_range(input):
    global ranges

    substrings = input.split('-')
    ranges.append((int(substrings[0]), int(substrings[1])))

def print_ranges():
    global ranges

    for r in ranges:
        print(str(r[0]) + "-" + str(r[1]))

def is_fresh(input):
    global ranges

    for r in ranges:
        if input >= r[0] and input <= r[1]:
            return True

    return False

count = 0

with open('2025/05/input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        # print(line)
        if line.count('-') > 0:
            add_range(line)
        elif len(line) == 0:
            # print_ranges()
            continue
        elif is_fresh(int(line)):
            count += 1
        
print(str(count))