import sys
import heapq
INF = int(10e9)
t = int(sys.stdin.readline().rstrip())
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))

    distance = [[INF] * n for _ in range(n)]
    q = [(board[0][0], 0, 0)]
    distance[0][0] = board[0][0]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + board[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])
