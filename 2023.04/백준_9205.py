from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    s_x, s_y = map(int, input().split())
    conv = []
    for _ in range(n):
        x, y = map(int, input().split())
        conv.append((x, y))
    end_x, end_y = map(int, input().split())
    queue = deque([(s_x, s_y, 20)])
    visited = [False] * n
    answer = "sad"
    while queue:
        x, y, beer = queue.popleft()

        dist = abs(x - end_x) + abs(y - end_y)
        if dist <= 1000:
            answer = "happy"
            break

        for i, c in enumerate(conv):
            if not visited[i] and (abs(x - c[0]) + abs(y - c[1])) <= 1000:
                visited[i] = True
                queue.append((c[0], c[1], 20))

    print(answer)