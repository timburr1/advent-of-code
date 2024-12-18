
def count(mem):
    seen = set()
    c = 0

    while not {tuple(mem)} <= seen:
        seen.add(tuple(mem))
        max = -1
        max_idx = -1

        for i in range(len(mem)):
            if mem[i] > max:
                max = mem[i]
                max_idx = i

        mem[max_idx] = 0
        for j in range(max):
            mem[(max_idx + j + 1) % len(mem)] += 1
        c += 1
    # print(str(mem))
    return c

mem = []
with open('2017/06/input.txt') as fp:
    for line in fp:
        for s in line.split():
            mem.append(int(s))
print(str(mem))
print(count(mem)) 

assert(count([0, 2, 7, 0]) == 5)
