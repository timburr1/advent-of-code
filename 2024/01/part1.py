
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

#print(list1)
#print(list2)

total_distance = 0

for n in range(len(list1)):
    total_distance += abs(int(list1[n]) - int(list2[n]))

print(total_distance)
