
input = ''
test_input = ''
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def reactive(first, second):
    global letters
    
    a = letters.find(first)
    b = letters.find(second)

    if a < b:
        return b - a == 26
    return a - b == 26

def react():
    global test_input

    for i in range(1, len(test_input)):
        if reactive(test_input[i], test_input[i-1]):
            test_input = test_input[:i-1] + test_input[i+1:]
            return False
    return True

def process():
    done = react() 
    while not done:
        done = react()
    
with open('2018/05/input.txt') as fp:
    for line in fp:
        input = line.replace('\n', '')
        
min_length = 1000000
for i in range (0, 26):
    test_input = input.replace(letters[i], '').replace(letters[i+26], '') 
    # print(letters[i] + ' / ' + letters[i+26])
    process()
    if len(test_input) < min_length:
        min_length = len(test_input)
    
print(str(min_length))
