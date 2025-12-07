
def biggest_digit(input):
    for i in range(9, 1, -1):
        if input.count(str(i)) >= 1:
            return i
    return 0

def max_joltage(input):
    max_digit = biggest_digit(input[len(input)-11])
    indices = []
    for i in range(0, len(input)):
        if input[i] == str(max_digit):
            indices.append(i)
    
    max = 0
    for i in indices:
        mj = something(input[i:])
        if mj > max:
            max = mj
    return max

sum = 0
with open('2025/03/input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        # print(line)
        sum += max_joltage(line) 
print(str(sum))