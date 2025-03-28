def solution(emergency):
    result = []
    
    for i in emergency:
        rank = 1
        
        for other in emergency:
            if other > i:  
                rank += 1
        result.append(rank)
    
    return result