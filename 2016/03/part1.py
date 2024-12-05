
def is_possible_tri(input):
    sides = ' '.join(input.split()).split(' ')
    # print(sides)
    a = int(sides[0])
    b = int(sides[1])
    c = int(sides[2])

    if a >= b and a >= c and a < b+c:
        return True
    
    if b >= a and b >= c and b < a+c:
        return True
    
    if c >= a and c >= b and c < a+b:
        return True

    return False

count = 0

with open('2016/03/input.txt') as fp:
    for line in fp:
        # print(line.replace('\n', ''))
        if is_possible_tri(line.replace('\n', '')):
            count += 1

print(str(count))
