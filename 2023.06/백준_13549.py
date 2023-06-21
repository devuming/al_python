from collections import deque
n, k = map(int, input().split())
visited = [False] * int(200001)
queue = deque([(n, 0)])
visited[n] = True

while queue:
    now, sec = queue.popleft()
    print(now, sec)
    if now == k:
        print(sec)
        break
    if now * 2 < len(visited) and not visited[now * 2]:
        queue.append((now * 2, sec))
        visited[now * 2] = True
    if now - 1 >= 0 and not visited[now - 1]:
        queue.append((now - 1, sec + 1))
        visited[now - 1] = True
    if now + 1 < len(visited) and not visited[now + 1]:
        queue.append((now + 1, sec + 1))
        visited[now + 1] = True

