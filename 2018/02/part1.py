
def check_for_double(id):
    for c in id:
        if id.count(c) == 2:
            return True
    return False

def check_for_triple(id):
    for c in id:
        if id.count(c) == 3:
            return True        
    return False

ids = []

with open('2018/02/input.txt') as fp:
    for line in fp:
        ids.append(line.replace('\n', ''))

double_count = 0
triple_count = 0
for id in ids:
    if check_for_double(id):
        double_count += 1
    if check_for_triple(id):
        triple_count += 1

print(str(double_count * triple_count))