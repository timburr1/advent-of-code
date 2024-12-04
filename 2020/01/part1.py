
nums = []

with open('2020/01/input.txt') as fp:
    for line in fp:
        #print(line)
        nums.append(int(line.replace('\n', '')))

for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(str(nums[i] * nums[j]))
            break
