
def check(input):
    for i in range(3, len(input)):
        if input[i] != input[i-1] and input[i] != input[i-2] and input[i] != input[i-3] and input[i-1] != input[i-2] and input[i-1] != input[i-3] and input[i-2] != input[i-3]:
            return i + 1

with open('2022/06/input.txt') as fp:    
    for line in fp:
        print(str(check(line.replace('\n', ''))))
