
ingredients = []

def add_ingredient(input):
    global ingredients

    input = input.replace(' capacity ', '').replace(' durability ', '').replace(' flavor ', '').replace(' texture ', '').replace(' calories ', '')
    a = input.split(':')
    name = a[0]
    b = a[1].split(',')
    # name, capacity, durability, flavor, texture, cals
    ingredients.append([name, b[0], b[1], b[2], b[3], b[4]])

with open('2015/15/input.txt') as fp:    
    for line in fp:
        add_ingredient(line.strip())

print(str(ingredients))
            