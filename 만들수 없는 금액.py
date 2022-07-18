# 만들수 없는 금액
n = int(input())
coin = list(map(int, input().split()))
coin.sort()

result = 1
for x in coin:
    if result < x:
        break
    result += x

print(result)