import sys
n, s, r = map(int, sys.stdin.readline().rstrip().split())
son = list(map(int, sys.stdin.readline().rstrip().split()))
more = list(map(int, sys.stdin.readline().rstrip().split()))

team = {i + 1:1 for i in range(n)}
for i in range(s):
    team[son[i]] -= 1
for i in range(r):
    team[more[i]] += 1

count = 0
for k, v in team.items():
    if v > 0:
       count += 1
    else:
        if team.get(k - 1, 0) > 1:
           team[k - 1] -= 1
           team[k] += 1
           count += 1
        elif team.get(k + 1, 0) > 1:
           team[k + 1] -= 1
           team[k] += 1
           count += 1
           
print(n - count)