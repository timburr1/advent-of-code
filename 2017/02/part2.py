
def check_line(input):
    vals = input.split()
    # print(str(vals))
    for i in range(0, len(vals)):
        for j in range(i+1, len(vals)):
            if int(vals[i]) % int(vals[j]) == 0:
                # print(str(vals[i]) + ' / ' + str(vals[j]))
                return int(vals[i]) / int(vals[j])
            elif int(vals[j]) % int(vals[i]) == 0:
                # print(str(vals[j]) + ' / ' + str(vals[i]))
                return int(vals[j]) / int(vals[i])

sum = 0
with open('2017/02/input.txt') as fp:
    for line in fp:
        sum += check_line(line)
print(int(sum))
        