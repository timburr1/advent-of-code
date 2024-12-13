
mols = set()
rules = dict()

def add_rule(input):
    global rules

    parts = input.split(' => ')
    if rules.get(parts[0]) == None:
        rules[parts[0]] = set()
    rules[parts[0]].add(parts[1])

def react(input):
    global mols, rules

    skip = False
    for i in range(len(input)):
        if skip:
            skip = False
            continue

        key = input[i]
        if i < len(input)-1 and input[i+1].islower():
            key += input[i+1]
            skip = True            
        if rules.get(key) == None:
            continue
        for r in rules[key]:
            if skip:
                mols.add(input[:i] + r + input[i+2:])
            else:
                mols.add(input[:i] + r + input[i+1:])

with open('2015/19/test2.txt') as file:
    for line in file:
        if line.count('=>') > 0:
            add_rule(line.replace('\n', ''))
        elif line == '\n':
            continue
        else:
            react(line.replace('\n', ''))

# print(str(rules))
# print(str(mols))
print(str(len(mols)))
