
input = '1'

def look_and_say(input):
    result = ''

    i = 0
    while i < len(input):
        num = input[i]

        j = i
        while j <= len(input)-1 and input[i] == input[j]:
            j += 1

        result += str(j-i) + str(num)
        i = j

    # print(result)
    return str(result)

result = look_and_say(input)
for i in range(49): 
    result = look_and_say(result)

print(str(len(result)))
