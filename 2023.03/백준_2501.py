
n, k = map(int, input().split())
i = 1
cnt = 0
while i <= n:
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break

    i += 1
if cnt < k:
    print(0)