
safe_count = 0

def all_increasing(readings):
    for i in range(1, len(readings)):
        if int(readings[i]) <= int(readings[i-1]):
            #print('Not increasing: ' + str(readings))
            return False

    return True

def all_decreasing(readings):
    for i in range(1, len(readings)):
        if int(readings[i]) >= int(readings[i-1]):
            #print('Not decreasing: ' + str(readings[i-1]) + ', ' + str(readings[i]))
            return False

    return True

def adjacent_diffs_valid(readings):
    for i in range(1, len(readings)):
        if abs(int(readings[i]) - int(readings[i-1])) > 3:
            return False

    return True

def check(str):
    global safe_count

    readings = str.replace('\n', '').split(' ')

    if not (all_increasing(readings) or all_decreasing(readings)):
        #print('Not increasing/decreasing: ' + str)
        return  
    
    if not adjacent_diffs_valid(readings):
        #print('Invalid distance: ' + str)
        return

    #print('Safe: ' + str)
    safe_count += 1

with open('2024/02/input.txt') as fp:
    for line in fp:
        check(line)

print(safe_count)