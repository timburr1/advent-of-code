import copy 

def count(mem):
    target = copy.deepcopy(mem)
    c = 0

    while True:
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
        if target == mem:
            break
    print(str(mem))
    print(c)
    return c

count([1, 0, 14, 14, 12, 12, 10, 10, 8, 8, 6, 6, 4, 3, 2, 1])
      
assert(count([2, 4, 1, 2]) == 4)
