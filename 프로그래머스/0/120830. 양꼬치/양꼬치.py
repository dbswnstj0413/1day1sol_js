def solution(n, k):
    free = n//10
    answer = (12000 * n) + ((k - free) * 2000)
    return answer