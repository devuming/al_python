# 초콜릿 식사
import sys
k = int(sys.stdin.readline().rstrip())
size = 1

while size < k:
    size *= 2 

print(size, end=' ')
count = 0       # 자른 횟수

while k > 0:
    if k >= size:
        k -= size
    else:
        count += 1
        size //= 2

print(count)