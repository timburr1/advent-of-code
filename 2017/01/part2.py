
def evaluate(input):
    sum = 0

    for i in range(0, len(input)):
        j = (i + int(len(input)/2)) % len(input)
        if input[i] == input[j]:
            sum += int(input[i])

    return sum

# print(str(evaluate('12131415')))

with open('2017/01/input.txt') as fp:
    for line in fp:
        print(str(evaluate(line.replace('\n', ''))))
        