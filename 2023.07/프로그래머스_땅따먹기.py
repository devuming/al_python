def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            max_value = -1
            for k in range(4):
                if j == k:
                    continue
                max_value = max(max_value, land[i-1][k])
            land[i][j] += max_value

    answer = max(land[len(land) - 1])
    return answer


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))  # 16
print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 1, 2], [5, 4, 3, 3]]))
