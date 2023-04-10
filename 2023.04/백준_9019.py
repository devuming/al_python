# DSLR
import sys
from collections import deque
def func_D(n):
    return (2 * n) % 10000
def func_S(n):
    return n - 1 if n > 0 else 9999
def func_L(n):
    # 천의 자리 숫자를 일의 자리로
    return (n % 1000 * 10) + (n // 1000)   
def func_R(n):
    # 일의 자리 숫자를 천의 자리로
    return (n % 10 * 1000)+ (n // 10)   

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    visited = [False] * (10000)
    a, b = map(int, sys.stdin.readline().rstrip().split())
    queue = deque()
    visited[a] = True
    queue.append((a, ""))

    # a->b로 변하는 경우의 수 탐색
    while queue:
        now, cmd = queue.popleft()

        if now == b:
            print(cmd)
            break

        now_D = func_D(now)
        now_S = func_S(now)
        now_L = func_L(now)
        now_R = func_R(now)

        if not visited[now_D]:
            visited[now_D] = True
            queue.append((now_D, cmd + "D"))

        if not visited[now_S]:
            visited[now_S] = True
            queue.append((now_S, cmd + "S"))

        if not visited[now_L]:
            visited[now_L] = True
            queue.append((now_L, cmd + "L"))

        if not visited[now_R]:
            visited[now_R] = True
            queue.append((now_R, cmd + "R"))