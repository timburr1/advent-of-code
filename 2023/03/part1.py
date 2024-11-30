SYMBOLS = {'@', '#', '$', '%', '&', '*', '/', '+', '-', '='}
grid = []

def checkForSymbols(rowNum, start, end):
    #print("checking: " + str(rowNum) + ", " + str(start) + ", " + str(end))

    if rowNum > 0:
        thisRow = grid[rowNum - 1]
        for i in range(start-1, end+2):
            if(i < 0 or i >= len(thisRow)):
                continue
            
            if(thisRow[i] in SYMBOLS):
                return True
    
    thisRow = grid[rowNum]
    for i in range(start-1, end+2):
        if(i < 0 or i >= len(thisRow)):
            continue
            
        if(thisRow[i] in SYMBOLS):
            return True

    if rowNum < len(grid) - 1:
        thisRow = grid[rowNum + 1]
        for i in range(start-1, end+2):
            if(i < 0 or i >= len(thisRow)):
                continue
            
            if(thisRow[i] in SYMBOLS):
                return True

    return False

def sumPartNumbers(lineNum, line):
    sum = 0
    thisNum = 0
    readingNum = False

    for i in range(0, len(line)):
        if line[i] >= '0' and line[i] <= '9':
            if not readingNum:
                readingNum = True
                thisNum = 0
                start = i

            thisNum *= 10
            thisNum += int(line[i])
        elif readingNum:
            readingNum = False
            end = i - 1

            if(checkForSymbols(lineNum, start, end)):
                if(lineNum < 10):
                    print("adding: " + str(thisNum))
                sum += thisNum

    return sum

with open('input.txt') as fp:
    for line in fp:
        grid.append(line)

    sum = 0
    for i in range(len(grid)):
        sum += sumPartNumbers(i, grid[i])
    print(sum)

    