
max = -1

with open('input.txt') as fp:
    sum = 0
    for line in fp:
        if line == '\n':
            if sum > max:
                max = sum
            sum = 0
        else:
            sum += int(line)

    # check one more time:
    if sum > max:
        max = sum

print(max)
