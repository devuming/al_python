import sys
from collections import deque
f, s, g, u, d = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * 1000001
answer = -1
queue = deque([(s, 0)])
visited[s] = True
while queue:
    now, cnt = queue.popleft()
    if now == g:
        answer = cnt
        break

    if now + u <= f and not visited[now + u]:
        visited[now + u] = True
        queue.append((now + u, cnt + 1))
    if now - d > 0 and not visited[now - d]:
        visited[now - d] = True
        queue.append((now - d, cnt + 1))
        
if answer == -1:
    print("use the stairs")
else:
    print(answer)