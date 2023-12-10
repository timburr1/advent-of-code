
def valueOf(input):
    minIdx = len(input)

    # todo: there is absolutely a cleverer way to do this...
    thisIdx = input.find("0")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 0
        minIdx = thisIdx
    thisIdx = input.find("one")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 1
        minIdx = thisIdx
    thisIdx = input.find("1")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 1
        minIdx = thisIdx
    thisIdx = input.find("two")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 2
        minIdx = thisIdx
    thisIdx = input.find("2")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 2
        minIdx = thisIdx    
    thisIdx = input.find("three")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 3
        minIdx = thisIdx
    thisIdx = input.find("3")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 3
        minIdx = thisIdx
    thisIdx = input.find("four")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 4
        minIdx = thisIdx
    thisIdx = input.find("4")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 4
        minIdx = thisIdx
    thisIdx = input.find("five")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 5
        minIdx = thisIdx
    thisIdx = input.find("5")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 5
        minIdx = thisIdx
    thisIdx = input.find("six")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 6
        minIdx = thisIdx
    thisIdx = input.find("6")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 6
        minIdx = thisIdx
    thisIdx = input.find("seven")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 7
        minIdx = thisIdx
    thisIdx = input.find("7")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 7
        minIdx = thisIdx
    thisIdx = input.find("eight")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 8
        minIdx = thisIdx
    thisIdx = input.find("8")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 8
        minIdx = thisIdx
    thisIdx = input.find("nine")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 9
        minIdx = thisIdx
    thisIdx = input.find("9")
    if (thisIdx > -1 and thisIdx < minIdx):
        leftVal = 9
        minIdx = thisIdx

    maxIdx = -1
    thisIdx = input.rfind("0")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 0
        maxIdx = thisIdx
    thisIdx = input.rfind("one")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 1
        maxIdx = thisIdx
    thisIdx = input.rfind("1")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 1
        maxIdx = thisIdx
    thisIdx = input.rfind("two")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 2
        maxIdx = thisIdx
    thisIdx = input.rfind("2")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 2
        maxIdx = thisIdx    
    thisIdx = input.rfind("three")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 3
        maxIdx = thisIdx
    thisIdx = input.rfind("3")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 3
        maxIdx = thisIdx
    thisIdx = input.rfind("four")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 4
        maxIdx = thisIdx
    thisIdx = input.rfind("4")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 4
        maxIdx = thisIdx
    thisIdx = input.rfind("five")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 5
        maxIdx = thisIdx
    thisIdx = input.rfind("5")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 5
        maxIdx = thisIdx
    thisIdx = input.rfind("six")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 6
        maxIdx = thisIdx
    thisIdx = input.rfind("6")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 6
        maxIdx = thisIdx
    thisIdx = input.rfind("seven")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 7
        maxIdx = thisIdx
    thisIdx = input.rfind("7")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 7
        maxIdx = thisIdx
    thisIdx = input.rfind("eight")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 8
        maxIdx = thisIdx
    thisIdx = input.rfind("8")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 8
        maxIdx = thisIdx
    thisIdx = input.rfind("nine")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 9
        maxIdx = thisIdx
    thisIdx = input.rfind("9")
    if (thisIdx > -1 and thisIdx > maxIdx):
        rightVal = 9
        maxIdx = thisIdx

    return leftVal * 10 + rightVal

sum = 0

with open('input.txt') as fp:
    for line in fp:
        # print(line)
        sum += valueOf(line)
        
print(str(sum))
