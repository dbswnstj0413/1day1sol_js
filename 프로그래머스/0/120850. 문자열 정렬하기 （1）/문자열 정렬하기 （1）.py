def solution(my_string):
    answer = []
    for char in my_string:
        if char.isdigit(): #isdigit() = 문자가 숫자라면 True를 반환한다.
            answer.append(int(char))
    answer.sort()
    return answer
