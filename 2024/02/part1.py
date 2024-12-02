
safe_count = 0

def all_increasing(readings):
    for i in range(1, len(readings)):
        if readings[i] <= readings[i-1]:
            return false

    return true

def all_decreasing(readings):
    for i in range(1, len(readings)):
        if readings[i] >= readings[i-1]:
            return false

    return true

def check(str):
    readings = str.replace('\n', '').split(' ')

    if not all_increasing(readings) and not all_decreasing(readings):
        return  
    
    if too_far_apart(readings):
        return

    safe_count += 1

with open('test.txt') as fp:
    for line in fp:
        check(line)

print(safe_count)