
def extrapolate_value(line: str) -> int:
    seqs = []
    steps = [int(n) for n in line.split()]
    while len(steps) > 0 and set(steps) != {0}:
        seqs.append(steps)
        steps = [steps[i + 1] - steps[i] for i in range(len(steps) - 1)]
    
    sum = 0
    for seq in seqs[::-1]:
        sum += seq[-1]
    return sum
    

sum = 0

with open('input.txt') as file:
    for line in file:
        #print(line)
        sum += extrapolate_value(line.strip())
        
print(str(sum))
