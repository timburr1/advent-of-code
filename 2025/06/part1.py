
lines = []

def add(index):
    global lines

    sum = 0
    for l in lines:
        if len(l[index]) == 0 or l[index] == '+':
            continue
        sum += int(l[index])
    return sum

def multiply(index):
    global lines

    prod = 1
    for l in lines:
        if len(l[index]) == 0 or l[index] == '*':
            continue
        prod *= int(l[index])
    return prod


with open('2025/06/input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        # print(line)
        lines.append(line.split())

hw_total = 0
signs  = lines[len(lines)-1]

for i in range(len(signs)):
    if signs[i] == "+":
        hw_total += add(i)
    else: # "*"
        hw_total += multiply(i)

print(str(hw_total))
        