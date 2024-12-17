
def count_steps(offsets):
    count = 0
    idx = 0

    while idx >= 0 and idx < len(offsets):
        instruction = offsets[idx]
        offsets[idx] = instruction + 1
        idx += instruction
        count += 1
    return count

offsets = []
with open('2017/05/input.txt') as fp:
    for line in fp:
        offsets.append(int(line.strip()))
#print(str(offsets))
print(count_steps(offsets))
