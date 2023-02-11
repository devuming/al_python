# 백준 2559_수열
# 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값
import sys
answer = -10e9
n, k = map(int, sys.stdin.readline().rstrip().split())
temp = list(map(int, sys.stdin.readline().rstrip().split()))
sums = [0] * (n + 1)
for i in range(1, n + 1):
    sums[i] = sums[i - 1] + temp[i - 1]

left = 0
right = left + k
while right <= n:
    answer = max(answer, sums[right] - sums[left])

    left += 1
    right += 1
    
print(answer)