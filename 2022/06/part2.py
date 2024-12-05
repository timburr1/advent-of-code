
def check_location(input, n):
    for a in range(n-14, n):
        for b in range(a+1, n):
                if input[a] == input[b]:
                    print(str(input[a]) + ', ' + str(input[b]))
                    return False
    return True

def check_string(input):
    for n in range(14, len(input)+1):
        if check_location(input, n):
            return str(n)

with open('2022/06/input.txt') as fp:    
    for line in fp:
        print(check_string(line.replace('\n', '')))


