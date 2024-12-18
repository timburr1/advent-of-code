
instructions = []

def check_overlap(rect1, rect2):
    a = rect1.split(' @ ')
    b = a[1].split(': ')
    c = b[0].split(',')
    x1 = int(c[0])
    y1 = int(c[1])
    d = b[1].split('x')
    w1 = int(d[0])
    h1 = int(d[1])

    a = rect2.split(' @ ')
    b = a[1].split(': ')
    c = b[0].split(',')
    x2 = int(c[0])
    y2 = int(c[1])
    d = b[1].split('x')
    w2 = int(d[0])
    h2 = int(d[1])

    if x1 + w1 <= x2:
        return False
    if x2 + w2 <= x1:
        return False
    if y1+ h1 <= y2:
        return False
    if y2 + h2 <= y1:
        return False
    
    return True

with open('2018/03/input.txt') as fp:
    for line in fp:
        instructions.append(line.strip())

for i in range(len(instructions)):
    overlap = False

    for j in range(len(instructions)):
        if i == j:
            continue
        
        if check_overlap(instructions[i], instructions[j]):
            overlap = True
            break
    
    if not overlap:
        print(str(i+1))
        break
            