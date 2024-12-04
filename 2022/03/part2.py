
chars =' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0
lines = []

def evaluate(str1, str2, str3):
    global sum, chars
    
    for c in str1:
        if str2.find(c) > -1 and str3.find(c) > -1:
            # print(c)
            sum += chars.find(c) 
            return

with open('2022/03/input.txt') as fp:
    for line in fp:
        lines.append(line.replace('\n', ''))

for i in range(0, len(lines) - 2, 3):
    # print('testing ' + str(i))
    evaluate(lines[i], lines[i+1], lines[i+2])

print(str(sum))        