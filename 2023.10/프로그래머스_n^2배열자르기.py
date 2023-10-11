def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        if i % n > i // n:
            answer.append(i % n + 1)
        else:
            answer.append(i // n + 1)
    return answer


print(solution(3, 2, 5))  # [3,2,2,3]
print(solution(4, 7, 14))  # [4,3,3,3,4,4,4,4]
