
def search(target):
    x = 0
    y = 0 
    c = 1
    v = 1
    while c < target:
        x += v
        c +=1 
        if c == 361527:
            break

        y += v
        c += 1
        if c == 361527:
            break

        x -= (v+1)
        c += 1
        if c == 361527:
            break

        y -= (v+1)
        c += 1

        v += 1
        
    print(str(abs(x) + abs(y)))

search(1)
search(12)
search(23)
search(1024)