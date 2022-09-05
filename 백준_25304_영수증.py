# 백준_25304_영수증
x = int(input())    # 금액
n = int(input())    # 갯수

total = 0

for _ in range(n):
    a, b = map(int, input().split())
    total += a * b

if total == x:
    print('Yes')
else:
    print('No')