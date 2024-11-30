
def valueOf(str):
    result = 0
    for c in str:
        if c >= "0" and c <= "9":
            result = 10 * int(c)
            break
    
    for c in str[::-1]:
        if c >= "0" and c <= "9":
            result += int(c)
            break
    
    return result

sum = 0

with open('input.txt') as fp:
    for line in fp:
        # print(line)
        sum += valueOf(line)
        
print(str(sum))
