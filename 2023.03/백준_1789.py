# 서로 다른 N개의 자연수의 합이 S일 때, 자연수 N의 최댓값
import sys
s = int(sys.stdin.readline().rstrip())
n = 0
total = 0
while total <= s:
    n += 1
    total += n
print(n - 1)