
def check(input):
    parts = input.split(': ')
    password = parts[1]
    sub_parts = parts[0].split(' ')
    letter = sub_parts[1]
    nums = sub_parts[0].split('-')
    i = int(nums[0]) - 1
    j = int(nums[1]) - 1

    if password[i] == letter and password[j] != letter:
        return True
    if password[i] != letter and password[j] == letter:
        return True
    return False

count = 0
with open('2020/02/input.txt') as fp:
    for line in fp:
        if check(line.replace('\n', '')):
            count += 1
print(str(count))
