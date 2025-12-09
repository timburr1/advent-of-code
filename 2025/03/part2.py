def max_joltage(bank):
    current_pos = 0
    digits_needed = 12
    result = ""

    # Loop 12 times to pick 12 digits
    for i in range(digits_needed):
        # We need to pick a digit, but we must leave enough room 
        # for the remaining digits we need to find later.
        remaining_after_this = digits_needed - 1 - i
        
        # Define the search window:
        # Start at current_pos
        # End early enough to leave 'remaining_after_this' characters
        search_limit = len(bank) - remaining_after_this
        
        # Get the valid slice of the string
        chunk = bank[current_pos : search_limit]
        
        # Find the largest digit in this chunk (e.g., '9')
        best_digit = max(chunk)
        
        # Add it to our result
        result += best_digit
        
        # UPDATE POSITION: Move our pointer to just after the digit we found.
        # chunk.index(best_digit) gives the first occurrence in the chunk.
        current_pos += chunk.index(best_digit) + 1

    return int(result)

total_sum = 0
with open('2025/03/input.txt') as file:
    for line in file:
        line = line.strip() 
        if line:
            total_sum += max_joltage(line)

print(total_sum)