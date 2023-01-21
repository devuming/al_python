# 그리디_동전
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

answer = 0
i = n - 1

while k > 0:
    count = k // coins[i]
    
    if count > 0:
        k -= count * coins[i]
        answer += count

    i -= 1

print(answer)