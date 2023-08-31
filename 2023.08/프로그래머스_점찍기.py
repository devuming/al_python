import math


def solution(k, d):
    answer = 0
    a, b = 0, 0

    while a <= d:
        print(a, ' : ', math.ceil((d ** 2 - a ** 2) ** 0.5 // k) + 1)
        answer += math.ceil((d ** 2 - a ** 2) ** 0.5 // k) + 1
        a += k

    return answer


print(solution(2, 4))  # 6
print(solution(1, 5))  # 26
