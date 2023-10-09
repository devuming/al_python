def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    print(A)
    print(B)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer


print(solution([1, 4, 2], [5, 4, 4]))  # 29
print(solution([1, 2], [3, 4]))  # 10
print(solution([1, 2, 3, 4], [5, 8, 7, 6]))  # 60
