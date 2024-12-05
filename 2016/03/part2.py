
vals = []

def is_possible_tri(a, b, c):
    if a >= b and a >= c and a < b+c:
        return True    
    if b >= a and b >= c and b < a+c:
        return True    
    if c >= a and c >= b and c < a+b:
        return True
    return False

def update_vals(input):
    global vals
    vals.append( ' '.join(input.split()).split(' ') )

def check_vals():
    count = 0

    for i in range(0, len(vals) - 2, 3):
        if is_possible_tri(int(vals[i][0]), int(vals[i+1][0]), int(vals[i+2][0])):
            count += 1
        if is_possible_tri(int(vals[i][1]), int(vals[i+1][1]), int(vals[i+2][1])):
            count += 1
        if is_possible_tri(int(vals[i][2]), int(vals[i+1][2]), int(vals[i+2][2])):
            count += 1
    print(str(count))

with open('2016/03/input.txt') as fp:
    for line in fp:
        update_vals(line.replace('\n', ''))

#print(str(vals))       
check_vals()