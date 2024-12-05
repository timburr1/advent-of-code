
def check(input):
    parts = input.split(': ')
    password = parts[1]
    sub_parts = parts[0].split(' ')
    letter = sub_parts[1]
    nums = sub_parts[0].split('-')
    min = int(nums[0])
    max = int(nums[1])

    count = 0
    for c in password:
        if c == letter:
            count += 1
    
    return count >= min and count <= max

count = 0
with open('2020/02/input.txt') as fp:
    for line in fp:
        if check(line.replace('\n', '')):
            count += 1
print(str(count))
