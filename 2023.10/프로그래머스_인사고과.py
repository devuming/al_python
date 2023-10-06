def solution(scores):
    answer = 0
    wan = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    pre = 0
    for a, b in scores:
        if wan[0] < a and wan[1] < b:
            return -1
        if b >= pre:
            pre = b
            if a + b > wan[0] + wan[1]:
                answer += 1

    return answer + 1


print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))  # 4
print(solution([[2, 1], [2, 3], [3, 2], [3, 2], [2, 1]]))  # -1
print(solution([[2, 2], [2, 3], [3, 2], [3, 2], [2, 1]]))  # 4
print(solution([[3, 2], [2, 3], [3, 2], [3, 2], [2, 1]]))  # 1
# [2, 3][3, 2][2, 2][2, 1]
