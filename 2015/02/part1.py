
def calculate_area(string):
    side_lengths = string.split('x')
    total_area = (int(side_lengths[0]) * int(side_lengths[1]))
    smallest_side_area = total_area
    total_area *= 2
    # print("New side: " + str(total_area / 2) + ", Small side: " + str(smallest_side_area))

    this_area = int(side_lengths[1]) * int(side_lengths[2]) 
    total_area += this_area * 2
    if(this_area < smallest_side_area):
        smallest_side_area = this_area
    # print("New side: " + str(this_area) + ", Small side: " + str(smallest_side_area))

    this_area = int(side_lengths[0]) * int(side_lengths[2]) 
    total_area += this_area * 2
    if(this_area < smallest_side_area):
        smallest_side_area = this_area
    # print("New side: " + str(this_area) + ", Small side: " + str(smallest_side_area))

    total_area += smallest_side_area
    # print(total_area)
    return total_area
     
sum = 0

with open('input.txt') as fp:
    for line in fp:
        sum += calculate_area(line)

print(str(sum))