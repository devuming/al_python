import math


def solution(n, k):
    nums = [i for i in range(1, n + 1)]
    answer = []
    k -= 1      # 1번째 배열은 [1...n]
    while nums:
        a = k // math.factorial(n - 1)
        answer.append(nums[a])
        del nums[a]
        k = k % math.factorial(n - 1)
        n -= 1

    return answer


print(solution(3, 5))   # [3,1,2]
