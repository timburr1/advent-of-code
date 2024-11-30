
def contains_double_letter(line):
    for i in range((len(line)) - 2):
        if line[i] == line[i+2]:
            return True
    
    return False

def contains_double_pair(line):
    for i in range(len(line)-3):
        for j in range(i+2, len(line)-1):
            if line[i] == line[j] and line[i+1] == line[j+1]:
                return True

def is_nice(line):
    if not contains_double_letter(line):
        return False
    if not contains_double_pair(line):
        return False

    return True

nice_string_count = 0

with open("input.txt") as fp:
    for line in fp:
        if is_nice(line.strip()):
            nice_string_count += 1

print(str(nice_string_count))