
def blink(stones):
    new_stones = {'1': 0}
    for k, v in stones.items():
        if k == '0':
            new_stones['1'] += v
        elif len(k) % 2 == 0:
            h = int(len(k) / 2)
            if new_stones.get(k[:h]) == None:
                new_stones[k[:h]] = v
            else:
                new_stones[k[:h]] += v
            if new_stones.get(str(int(k[h:]))) == None:
                new_stones[str(int(k[h:]))] = v
            else:
                new_stones[str(int(k[h:]))] += v
        else:
            if new_stones.get(str(int(k) * 2024)) == None:
                new_stones[str(int(k) * 2024)] = v   
            else:
                new_stones[str(int(k) * 2024)] += v   
    return new_stones

# {'125': 1, '17': 1}
stones = {'27':1, '10647':1, '103':1, '9':1, '0':1, '5524':1, '4594227':1, '902936':1}
for i in range(75): 
    stones = blink(stones)
    # print(str(stones))
print(str(sum(stones.values())))
