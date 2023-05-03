import sys
n = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
edges = [[] for i in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    edges[x].append(y)
    edges[y].append(x)
visited = [False] * (n+1)
answer = -1
stk = [(a, 0)]
visited[a] = True
 
while stk :
    now, cnt = stk.pop()
    visited[now] = True
    if now == b:
        answer = cnt
        break

    for i in range(0, len(edges[now])):
        if not visited[edges[now][i]]:
            stk.append((edges[now][i], cnt + 1))
    
print(answer)