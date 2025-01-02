def fibonaci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, num):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence