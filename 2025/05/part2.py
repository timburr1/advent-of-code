ranges = []

def add_range(input_str):
    global ranges
    
    substrings = input_str.split('-')
    ranges.append((int(substrings[0]), int(substrings[1])))

def merge_ranges():
    global ranges
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])

    merged = []
    for current_start, current_end in ranges:
        if not merged:
            merged.append((current_start, current_end))
        else:
            last_start, last_end = merged[-1]

            if current_start <= last_end:
                new_end = max(last_end, current_end)
                merged[-1] = (last_start, new_end)
            else:
                merged.append((current_start, current_end))
    
    return merged

with open('2025/05/input.txt') as file:
    for line in file:
        line = line.strip()
        if '-' in line:
            add_range(line)
        else:
            continue

final_ranges = merge_ranges()

total_count = 0
for r in final_ranges:
    total_count += r[1] - r[0] + 1

print(total_count)