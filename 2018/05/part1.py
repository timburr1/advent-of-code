
input = ''

def reactive(first, second):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    a = letters.find(first)
    b = letters.find(second)

    if a < b:
        return b - a == 26
    return a - b == 26

def react():
    global input

    for i in range(1, len(input)):
        if reactive(input[i], input[i-1]):
            input = input[:i-1] + input[i+1:]
            return False
    return True

def process():
    done = react() 
    while not done:
        done = react()
    
with open('2018/05/input.txt') as fp:
    for line in fp:
        input = line.replace('\n', '')
        process()
        print(input)
        print(str(len(input)))
