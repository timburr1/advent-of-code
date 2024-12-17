
def search(target):
    i = 1
    while i * i <= target:
        i += 2
    i -= 2
    print(i)

# search(1)
# search(12)
# search(23)
# search(1024)
search(361527)

# part 2: https://oeis.org/A141481/b141481.txt