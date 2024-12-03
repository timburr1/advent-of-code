
top_three = []

with open('test.txt') as fp:
    
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
