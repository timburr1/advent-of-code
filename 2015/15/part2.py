
ingredients = []

def add_ingredient(input):
    global ingredients

    input = input.replace(' capacity ', '').replace(' durability ', '').replace(' flavor ', '').replace(' texture ', '').replace(' calories ', '')
    a = input.split(':')
    name = a[0]
    b = a[1].split(',')
    # name, capacity, durability, flavor, texture, cals
    ingredients.append([name, int(b[0]), int(b[1]), int(b[2]), int(b[3]), int(b[4])])

def score_cookie(a, b, c, d):
    global ingredients

    if ingredients[0][5]*a + ingredients[1][5]*b + ingredients[2][5]*c + ingredients[3][5]*d != 500:
        return -1
    
    capacity = max(ingredients[0][1]*a + ingredients[1][1]*b + ingredients[2][1]*c + ingredients[3][1]*d, 0)
    durability = max(ingredients[0][2]*a + ingredients[1][2]*b + ingredients[2][2]*c + ingredients[3][2]*d, 0)
    flavor = max(ingredients[0][3]*a + ingredients[1][3]*b + ingredients[2][3]*c + ingredients[3][3]*d, 0)
    texture = max(ingredients[0][4]*a + ingredients[1][4]*b + ingredients[2][4]*c + ingredients[3][4]*d, 0)    

    return capacity * durability * flavor * texture

with open('2015/15/input.txt') as fp:    
    for line in fp:
        add_ingredient(line.strip())

max_score = -1
for a in range(0, 101):
    for b in range(0, 101):
        for c in range(0, 101):
            if a + b + c > 100:
                continue
            d = 100 - a - b - c          
            score = score_cookie(a, b, c, d)
            if score > max_score:
                max_score = score

print(str(max_score))