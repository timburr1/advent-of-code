
chars =' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0

def evaluate(input):
    global sum, chars

    half = int(len(input)/2)
    first = input[0:half]
    second = input[half:len(input)]

    for c in first:
        if second.find(c) > -1:
            sum += chars.find(c) 
            return

with open('2022/03/input.txt') as fp:
    for line in fp:
        evaluate(line.replace('\n', ''))

print(str(sum))        