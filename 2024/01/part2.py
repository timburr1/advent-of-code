
list1 = []
list2 = []

def insert(str):
    vals = str.split('   ')
    list1.append(vals[0])
    list2.append(vals[1].replace('\n', ''))

with open('2024/01/input.txt') as fp:
    for line in fp:
        insert(line)

list1 = sorted(list1)
list2 = sorted(list2)

total_similaryity = 0

for n in list1:
    similarity = int(n) * list2.count(n)
    total_similaryity += similarity

print(total_similaryity)
