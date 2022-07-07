# 소수 판별
# 에라타노스테네스의 체 : 범위 내의 모든 소수를 구할 수 있는 방법
# 1. 범위 루트값이내의 소수를 구함
# 2. 각 소수의 배수 제거
from math import sqrt
def solution(end):
    answer = [True for _ in range(end + 1)]

    # 7 - 10 : 1
    for n in range(2, int(sqrt(end)) + 1):
        if answer[n]:
            i = 2
            while (n * i) <= end:
                answer[(n * i)] = False   # 배수 제거
                i += 1
            print(answer)


    return [i for i in range(2, end + 1) if answer[i]]

print(solution(26))
print(solution(27))