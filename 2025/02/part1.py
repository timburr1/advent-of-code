
def is_invalid(s):
    l = len(s)
    m = int(l/2)
    return s[:m] == s[m:]

sum = 0

with open('2025/02/input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        # print(line)
        ranges = line.split(',')

        for r in ranges:
            vals = r.split('-')
            min = int(vals[0])
            max = int(vals[1])

            for i in range(min, max+1):
                if is_invalid(str(i)):
                    sum += i

print(str(sum))