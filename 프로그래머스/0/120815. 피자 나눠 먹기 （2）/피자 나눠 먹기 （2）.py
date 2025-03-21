def solution(n):
    pieces = 6
    pizza = 1
    while (pieces * pizza) % n != 0:
        pizza = pizza + 1
    return pizza
