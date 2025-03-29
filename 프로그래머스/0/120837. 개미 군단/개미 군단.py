def solution(hp):
    five_ant = hp // 5
    three_ant = (hp % 5) // 3
    one_ant = (hp % 5) % 3
    answer = five_ant + three_ant + one_ant
    return answer