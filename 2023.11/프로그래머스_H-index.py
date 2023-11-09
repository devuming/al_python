def solution(citations):
    left, right = 0, len(citations)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        h_cnt = 0
        for i, cit in enumerate(citations):
            if mid <= cit:
                h_cnt += 1
        if mid <= h_cnt:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer


print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([0, 1, 1, 1, 3, 4]))  # 2
