import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
score = []
for _ in range(n):
    score.append(list(map(int, sys.stdin.readline().rstrip().split())))
score.sort(key=lambda x:(-x[1], -x[2], -x[3]))

idx = -1
for i in range(n):
    if score[i][0] == k:
        idx = i
        break

for i in range(n):
    if score[idx][1:] == score[i][1:]:
        print(i + 1)
        break