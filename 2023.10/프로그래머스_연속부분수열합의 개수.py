def solution(elements):
    answer = set()
    n = len(elements)
    arr = elements * 2
    # print(arr)
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] + arr[i]

    # print(arr)
    for i in range(1, n + 1):
        for j in range(n):
            answer.add(arr[j + i] - arr[j])
        # print(arr[j + i] - arr[j])

    return len(answer)


print(solution([7, 9, 1, 1, 4]))  # 18
