def solution(order):
    answer = 0
    stk = []
    last = -1

    for i, o in enumerate(order):
        if last < o:
            for j in range(last + 1, o):
                stk.append(j)
            last = o
            answer += 1
        elif stk[-1] == o:
            answer += 1
            stk.pop()
        else:
            break
    return answer


print(solution([4, 3, 1, 2, 5]))    # 2
print(solution([5, 4, 3, 2, 1]))    # 5
print(solution([4, 2, 1, 5, 3]))    # 1
print(solution([3, 2, 1, 4, 5]))    # 5
print(solution([3, 2, 1, 5, 4]))    # 5
