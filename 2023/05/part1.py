
maps = []
def lookup_location(initial_value: int) -> int:
    value = initial_value
    for current_map in maps:
        value = next(
            (destination_range.start + (value - source_range.start)
             for source_range, destination_range in current_map.items()
             if value in source_range),
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

seeds = []
for num in input_data[0].replace("seeds: ", "").split(" "):
    seeds.append(int(num))
locations = [lookup_location(seed) for seed in seeds]

print(min(locations))