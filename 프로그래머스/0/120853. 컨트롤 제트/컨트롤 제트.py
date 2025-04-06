def solution(s):
    answer = 0
    last_number = 0
    for token in s.split():
        if token == "Z":
            answer -= last_number
        else:
            last_number = int(token)
            answer += last_number
    
    return answer