
top_three = [-1, -1, -1]

def try_insert(num):
    if num > top_three[0]:
        top_three[2] = top_three[1]
        top_three[1] = top_three[0]
        top_three[0] = num
    elif num > top_three[1]:
        top_three[2] = top_three[1]
        top_three[1] = num
    elif num > top_three[2]:
        top_three[2] = num

with open('input.txt') as fp:
    sum = 0
    for line in fp:
        if line == '\n':
            try_insert(sum)
            sum = 0
        else:
            sum += int(line)

    # check one more time:
    try_insert(sum)

print(str(top_three[0] + top_three[1] + top_three[2]))
