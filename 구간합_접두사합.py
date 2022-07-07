# 구간합 - i 번째 ~ j 번째 데이터의 합을 구하는 프로그램
# O(NM) 복잡도 > O(N + M) 복잡도

def solution(nums, n, m):
    p = [0] * len(nums)     # p[i] : 미리 0 - i 번째 데이터의 합 구해놓기

    for i in range(len(nums)):
        if i - 1 < 0:
            p[i] = nums[i]
        else:
            p[i] = p[i - 1] + nums[i]
    
    return p[m] - p[n - 1] if n - 1 >= 0 else p[m]

print(solution([10, 20, 30, 40, 50], 2, 4))     # [10, 30, 60, 100, 150] 30 + 40 + 50 == 150 - 30 == 120
print(solution([10, 20, 30, 40, 50], 1, 2))     # [10, 30, 60, 100, 150] 20 + 30 == 60 - 10 == 50
print(solution([10, 20, 30, 40, 50], 0, 1))     # [10, 30, 60, 100, 150] 10 + 20 == 30 == 30 - 0