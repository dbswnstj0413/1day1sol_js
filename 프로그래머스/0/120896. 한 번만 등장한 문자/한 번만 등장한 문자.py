def solution(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    unique_chars = [char for char in count if count[char] == 1]
    
    unique_chars.sort()

    return ''.join(unique_chars)