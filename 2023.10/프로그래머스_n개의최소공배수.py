def gcd(a, b):
    if a % b == 0:
        return b

    return gcd(b, a % b)


def lcd(a, b):
    return a * b // gcd(a, b)


def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcd(answer, arr[i])

    return answer


print(solution([2, 6, 8, 14]))  # 168
print(solution([1, 2, 3]))
