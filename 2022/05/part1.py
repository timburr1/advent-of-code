
# [F]         [L]     [M]            
# [T]     [H] [V] [G] [V]            
# [N]     [T] [D] [R] [N]     [D]    
# [Z]     [B] [C] [P] [B] [R] [Z]    
# [M]     [J] [N] [M] [F] [M] [V] [H]
# [G] [J] [L] [J] [S] [C] [G] [M] [F]
# [H] [W] [V] [P] [W] [H] [H] [N] [N]
# [J] [V] [G] [B] [F] [G] [D] [H] [G]
#  1   2   3   4   5   6   7   8   9 

# stacks = ['', 'JHGMZNTF','VWJ','GVLJBTH','BPJNCDVL','FWSMPRG','GHCFBNVM','DHGMR','HNMVZD','GNFH']

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

stacks = ['', 'ZN', 'MCD', 'P']

def move(instruction):
    i = instruction.replace('move ', '').replace('from ', '').replace('to ', '')
    vals = i.split(' ')
    stacks[int(vals)]
    # print(str(vals))

with open('2022/05/test.txt') as fp:    
    for line in fp:
        move(line.replace('\n', ''))

result = ''
for s in stacks:
    result += s[-1:]
print(result)