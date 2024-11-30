
maps = []
def reverse_lookup_seed(location: int) -> int:
    value = location
    for current_map in reversed(maps):
        value = next(
            (source_range.start + (value - destination_range.start)
             for source_range, destination_range in current_map.items()
             if value in destination_range),
            value  # fallback
        )
    return value

with open('input.txt', 'r') as file:
    input_data = file.read().splitlines()

for line in input_data[2:]:
    if 'map' in line:
        maps.append(dict())
    elif line != '':
        destination, source, length = [int(value) for value in line.split()]
        maps[-1][range(source, source+length)] = range(destination, destination+length)


nums = input_data[0].replace("seeds: ", "").split(" ")
seed_ranges = []
for i in range(0, len(nums) - 1, 2):
    start = int(nums[i])
    length = int(nums[i+1])
    seed_ranges.append(range(start, start + length))

print(seed_ranges)

location = 0
while True:
    potential_seed = reverse_lookup_seed(location)
    if any(potential_seed in seed_range for seed_range in seed_ranges):
        print(location)
        break
    location += 1