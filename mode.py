def mode(numbers):
    if not numbers:
        return None
    
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    max_frequency = 0
    curr_mode = None

    for num, count in frequency.items():
        if count > max_frequency:
            max_frequency = count
            curr_mode = num
        
    return curr_mode