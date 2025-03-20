def solution(array):
    u = list(set(array))
    answer = []
    for v in u :
        answer.append(array.count(v))
    if answer.count(max(answer)) > 1 :
        return -1
    return u[answer.index(max(answer))]