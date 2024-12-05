
keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# starting location:
x = 1
y = 1

def process(input):
    global keypad, x, y

    for c in input:
        if c == 'U' and y > 0:
            y -= 1
        elif c == 'D' and y < 2:
            y += 1
        elif c == 'L' and x > 0:
            x -= 1
        elif c == 'R' and x < 2:
            x += 1 

    return keypad[y][x]

code = ''

with open('2016/02/input.txt') as fp:
    for line in fp:
        code += str(process(line.replace('\n', '')))

print(code)
        