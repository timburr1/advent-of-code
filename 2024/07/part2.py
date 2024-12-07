
sum = 0

def c(target, vals):
    
    if(len(vals) > 2):
        return c(target, [vals[0]+vals[1]]+vals[2:]) or c(target, [vals[0]*vals[1]]+vals[2:]) or c(target, [int(str(vals[0])+str(vals[1]))]+vals[2:])
    return vals[0] + vals[1] == target or vals[0] * vals[1] == target or int(str(vals[0]) + str(vals[1])) == target

def check(input):
    global sum

    i = input.split(': ')
    target = int(i[0])
    vals = i[1].split(' ')
    for i in range(0, len(vals)):
        vals[i] = int(vals[i])

    if c(target, vals):
        sum += target

with open('2024/07/input.txt') as fp:    
    for line in fp:
        check(line.replace('\n', ''))

print(str(sum))