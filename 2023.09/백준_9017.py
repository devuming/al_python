import sys
from collections import Counter
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    teams = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt = Counter(teams)
    score = {}
    minus = 0

    for i, team in enumerate(teams):
        if cnt[team] < 6:
            minus += 1
            continue
        if score.get(team):
            score[team].append(i + 1 - minus)
        else:
            score[team] = []
            score[team].append(i + 1 - minus)

    win = 10e9
    result = 0

    for k, v in score.items():
        total = 0
        for i in range(4):
            total += v[i]
        if total < win:
            result = k
            win = total
        elif total == win:
            if score[k][4] < score[result][4]:
                result = k

    print(result)
