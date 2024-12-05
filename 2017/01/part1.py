
def evaluate(input):
    sum = 0

    for i in range(0, len(input)-1):
        if input[i] == input[i+1]:
            sum += int(input[i])

    if input[0] == input[len(input)-1]:
        sum += int(input[0])

    return sum

# print(str(evaluate('91212129')))

with open('2017/01/input.txt') as fp:
    for line in fp:
        print(str(evaluate(line.replace('\n', ''))))
        