def solution(queue1, queue2):
    answer = -1
    queue = queue1 + queue2
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)

    left, right = 0, len(queue1)
    mid = (q1_sum + q2_sum) // 2
    while left <= right and right < len(queue):
        if mid - q1_sum < mid - q2_sum:
            q1_sum -= queue[left]
            q2_sum += queue[left]
            left += 1
        elif mid - q1_sum > mid - q2_sum:
            q1_sum += queue[right]
            q2_sum -= queue[right]
            right += 1
        if q1_sum == q2_sum:
            answer = left + (right - len(queue1))
            break

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))  # 7
print(solution([1, 1], [1, 5]))  # -1)
