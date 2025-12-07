
def check(string, num_substrings):
    substring_length = int(len(string) / num_substrings)

    for i in range(substring_length):
        for j in range(1, num_substrings):
            if string[i] != string[j*substring_length + i]:
                return False
    return True

def is_invalid(s):
    length = len(s)
    for i in range(2, length+1):
        if length % i != 0:
            continue
        
        if check(s, i):
            return True
        
    return False

sum = 0

with open('2025/02/input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        # print(line)
        ranges = line.split(',')

        for r in ranges:
            # print(r + ": ")
            vals = r.split('-')
            min = int(vals[0])
            max = int(vals[1])
            for i in range(min, max+1):
                if is_invalid(str(i)):
                    # print(str(i))
                    sum += i

print(str(sum))