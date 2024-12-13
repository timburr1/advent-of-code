from itertools import combinations

nums = []
with open('2015/17/input.txt') as fp:    
    for line in fp:
        # print(line.strip())
        nums.append(int(line.strip()))

count = 0
target = 150
for n in range(1, len(nums)+1):
    for c in combinations(nums, n):
        if sum(c) == target:
            count += 1
print(str(count))
# print(str(nums))