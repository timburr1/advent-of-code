
grid = []

def count_up(x, y):
    global grid

    score = 0
    for i in range(y-1, -1, -1):
        score += 1
        if grid[i][x] >= grid[y][x]:
            return score            
    return score
    
def count_down(x, y):
    global grid

    score = 0
    for i in range(y+1, len(grid)):
        score += 1
        if grid[i][x] >= grid[y][x]:
            return score
    return score

def count_left(x, y):
    global grid

    score = 0
    for i in range(x-1, -1, -1):
        score += 1
        if grid[y][i] >= grid[y][x]:
            return score
    return score

def count_right(x, y):
    global grid

    score = 0
    for i in range(x+1, len(grid[0])):
        score += 1
        if grid[y][i] >= grid[y][x]:
            return score
    return score

def score_tree(x, y):
    return count_up(x,y) * count_down(x,y) * count_left(x,y) * count_right(x,y)

with open('2022/08/input.txt') as fp:    
    for line in fp:
        this_row = []
        for c in line.strip():
            this_row.append(int(c))
        grid.append(this_row)

max_score = -1
for y in range(1, len(grid)-1):
    for x in range(1, len(grid[0])-1):
        score = score_tree(x, y)
        if score > max_score:
            max_score = score
print(str(max_score))
