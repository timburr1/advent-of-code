
VOWELS = {'a', 'e', 'i', 'o', 'u'}
def count_vowels(line):
    vowel_count = 0

    for i in range(len(line)):
        if line[i] in VOWELS:
            vowel_count += 1

    return vowel_count

def contains_double_letter(line):
    for i in range((len(line)) - 1):
        if line[i] == line[i+1]:
            return True
    
    return False

def contains_forbidden_string(line):
    if line.find("ab") >= 0:
        return True
    
    if line.find("cd")  >= 0:
        return True

    if line.find("pq")  >= 0:
        return True
    
    if line.find("xy")  >= 0:
        return True
    
    return False

def is_nice(line):
    if count_vowels(line) < 3:
        return False
    if not contains_double_letter(line):
        return False
    if contains_forbidden_string(line):
        return False

    return True

nice_string_count = 0

with open("input.txt") as fp:
    for line in fp:
        if is_nice(line.strip()):
            nice_string_count += 1

print(str(nice_string_count))