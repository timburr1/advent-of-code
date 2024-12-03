
safe_count = 0

def all_increasing(readings):
    for i in range(1, len(readings)):
        if int(readings[i]) <= int(readings[i-1]):
            return False

    return True

def all_decreasing(readings):
    for i in range(1, len(readings)):
        if int(readings[i]) >= int(readings[i-1]):
            return False

    return True

def adjacent_diffs_valid(readings):
    for i in range(1, len(readings)):
        if abs(int(readings[i]) - int(readings[i-1])) > 3:
            return False

    return True

def is_list_valid(readings):
    #print('Checking ' + str(readings))

    if not (all_increasing(readings) or all_decreasing(readings)):
        #print('Not increasing/decreasing: ' + str(readings))
        return False 
    
    if not adjacent_diffs_valid(readings):
        #print('Invalid distance: ' + str(readings))
        return False

    return True


def check(input):
    global safe_count

    readings = input.replace('\n', '').split(' ')
   
    if is_list_valid(readings):
        #print('Safe: ' + input)
        safe_count += 1
        return

    for i in range(0, len(readings)):
        temp = readings.copy()
        temp.pop(i)
        if is_list_valid(temp):
            #print('Safe: ' + str(temp))
            safe_count += 1
            return
    
with open('input.txt') as fp:
    for line in fp:
        check(line)

print(safe_count)