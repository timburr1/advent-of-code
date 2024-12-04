
nums = []

with open('2021/01/input.txt') as fp:
    for line in fp:
        nums.append(int(line.replace('\n', '')))

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1

print(str(count))
