
def max_joltage(input):
    max = 0

    for i in range(0, len(input)):
        for j in range(i+1, len(input)):
            joltage = int(input[i] + input[j])
            if joltage > max:
                max = joltage
    return max

sum = 0

with open('2025/03/input.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        # print(line)
        sum += max_joltage(line)
        
print(str(sum))