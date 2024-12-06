
min = 387638
max = 919123

def check_for_double(input):
    for i in range(1, len(input)):
        if input[i-1] == input[i]:
            return True
    return False

def check_increasing(input):
    for i in range(1, len(input)):
        if int(input[i-1]) > int(input[i]):
            return False
    return True

def check(input):
    if not check_for_double(input):
        return False
    if not check_increasing(input):
        return False
    return True

count = 0
for i in range(min, max+1):
    if check(str(i)):
        count += 1
print(str(count))
