# 백준_시험감독
import sys, math
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
b, c = map(int, sys.stdin.readline().rstrip().split())

answer = n  # 총 감독관

for a in arr:
    if a > b:
        answer += math.ceil((a - b) / c)

print(answer)