def solution(money):
    coffee = 5500
    max = money // 5500
    change = money % 5500
    return [max, change]