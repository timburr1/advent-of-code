import hashlib

# "abcdef"
# "pqrstuv"
input = "iwrupvqb" 
done = False
guess = 0

while not done:
    hash_str = str( hashlib.md5((input + str(guess)).encode()).hexdigest()  )
    # print(hash_str)

    if hash_str.startswith("00000"):
        print(str(guess))
        done = True
    # elif guess > 609045:
    #    print("failed to find...")
    #    done = True
    else:
        guess += 1

