
def blink(stones):
    for i in range(len(stones)):
        this_len = len(stones[i])    

        if stones[i] == '0':
            stones[i] = '1'
        elif this_len % 2 == 0:
            stones = stones[:i] + [stones[i][:int(this_len/2)]] + [stones[i][int(this_len/2):]] + stones[i+1:] 
            i += 1
        else:
            stones[i] = str(2024 * int(stones[i]))

    return stones

stones = ['0', '1', '10', '99', '999']
stones = blink(stones)
print(str(stones))