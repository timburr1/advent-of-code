from itertools import combinations

nums = []
with open('2015/17/input.txt') as fp:    
    for line in fp:
        # print(line.strip())
        nums.append(int(line.strip()))

counts = dict()
target = 150
for n in range(1, len(nums)+1):
    
    for c in combinations(nums, n):
        if sum(c) == target:
            if counts.get(n) == None:
                counts[n] = 0
            counts[n] += 1
min_key = min(counts.keys())
print(str(counts[min_key]))
# print(str(nums))