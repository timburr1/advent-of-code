
def overlap(input):
    ranges = input.split(',')
    range1 = ranges[0].split('-')
    range2 = ranges[1].split('-')

    if int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1]):
        return True
    
    if int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1]):
        return True
    
    return False

count = 0

with open('2022/04/input.txt') as fp:    
    for line in fp:
        if overlap(line.replace('\n', '')):
            # print(line)
            count += 1

print(str(count))