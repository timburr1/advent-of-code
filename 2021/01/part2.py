
nums = []

with open('2021/01/input.txt') as fp:
    for line in fp:
        nums.append(int(line.replace('\n', '')))

sums = []
for i in range(2, len(nums)):
    sums.append(nums[i] + nums[i-1] + nums[i-2])

count = 0

for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        count += 1

print(str(count))
