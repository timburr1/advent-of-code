
keypad = [['_', '_', '1', '_', '_'],
          ['_', '2', '3', '4', '_'],
          ['5', '6', '7', '8', '9'],
          ['_', 'A', 'B', 'C', '_'],
          ['_', '_', 'D', '_', '_']]
# starting location:
x = 0
y = 2

def process(input):
    global keypad, x, y

    for c in input:
        if c == 'U' and y > 0 and keypad[y-1][x] != '_':
            y -= 1
        elif c == 'D' and y < 4 and keypad[y+1][x] != '_':
            y += 1
        elif c == 'L' and x > 0 and keypad[y][x-1] != '_':
            x -= 1
        elif c == 'R' and x < 4 and keypad[y][x+1] != '_':
            x += 1 

    return keypad[y][x]

code = ''

with open('2016/02/input.txt') as fp:
    for line in fp:
        code += process(line.replace('\n', ''))

print(code)
        