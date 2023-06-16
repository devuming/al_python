# 의견 없으면 난이도 0
# 의견 있으면 모든 사람의 난이도 의견의 30% 절사평균(위아래 15% 제외하고 평균)
import sys


def new_round(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)


n = int(sys.stdin.readline().rstrip())
level = []
for _ in range(n):
    level.append(int(sys.stdin.readline().rstrip()))
level.sort()
idx = new_round(n * 0.15)
cnt = n - (2 * idx)

if cnt <= 0:
    print(0)
else:
    total = 0
    for i in range(idx, n - idx):
        total += level[i]

    answer = new_round(total / cnt)
    print(answer)
