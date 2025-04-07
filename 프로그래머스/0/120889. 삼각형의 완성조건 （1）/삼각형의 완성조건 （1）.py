def solution(sides):
    max_side = max(sides)
    other_sum = sum(sides) - max_side
    
    if max_side < other_sum:
        return 1  
    else:
        return 2 