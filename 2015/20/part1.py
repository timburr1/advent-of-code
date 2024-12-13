
target = 36000000

def presents_at(house_num):
    presents = 0

    for i in range(house_num, 0, -1):
        if house_num % i == 0:
            presents += 10 * i
    # print('House ' + str(house_num) + ' got ' + str(presents) + ' presents.')
    return presents

i = 110000
print(i)
presents = presents_at(i)
while presents < target:
    i += 1
    presents = presents_at(i)
print(i)
