
def check_line(input):
    min = 1000000
    max = -1

    vals = input.split()
    for v in vals:
        if int(v) < min:
            min = int(v)
        if int(v) > max:
            max = int(v)

    print(str(max) + ' - ' + str(min) + ' = ' + str(max-min))
    return max - min            

sum = 0
with open('2017/02/input.txt') as fp:
    for line in fp:
        sum += check_line(line)
print(int(sum))
        