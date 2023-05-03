n, new_s, p = map(int, input().split())
if n == 0:
    print(1)
    exit(0)

scores = list(map(int, input().split()))

answer = -1
if p == n and scores[-1] >= new_s:
    print(-1)
else:
    answer = n + 1
    for i in range(n):
        if scores[i] <= new_s:
            answer = i + 1
            break
    print(answer)