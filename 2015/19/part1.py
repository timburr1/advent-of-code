
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

    mols.add(input)
    # Todo: replace + react

with open('2015/19/test.txt') as file:
    for line in file:
        if line.count('=>') > 0:
            add_rule(line.replace('\n', ''))
        elif line == '\n':
            continue
        else:
            react(line.replace('\n', ''))

print(str(rules))
print(str(len(mols)))
