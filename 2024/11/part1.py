
def blink(stones):
    skip_next = False
    
    i = 0
    while i < len(stones):
        if skip_next:
            skip_next = False
            i += 1
            continue

        this_len = len(stones[i])    

        if stones[i] == '0':
            stones[i] = '1'
        elif this_len % 2 == 0:
            stones = stones[:i] + [str(int(stones[i][:int(this_len/2)]))] + [str(int(stones[i][int(this_len/2):]))] + stones[i+1:] 
            skip_next = True
        else:
            stones[i] = str(2024 * int(stones[i]))
        i += 1
    return stones

# ['0', '1', '10', '99', '999']
# ['125', '17'] 
stones = ['27', '10647', '103' ,'9', '0', '5524', '4594227', '902936']
for i in range(25):
    stones = blink(stones)
    # print(str(stones))
print(str(len(stones)))
