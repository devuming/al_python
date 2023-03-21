# Z
import sys
sys.setrecursionlimit(10**7)

n, r, c = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

def visitZ(x, y, n):
    global cnt
    if n == 1:
        if x == r and y == c:
            print(cnt)
            exit(0)
        cnt += 1
        return
    
    # 4개로 쪼개기
    if x <= r < (x + n) and y <= c < (y + n):
        mid = n // 2
        visitZ(x, y, mid)
        visitZ(x, y + mid, mid)
        visitZ(x + mid, y, mid)
        visitZ(x + mid, y + mid, mid)
    else:
        cnt += n * n
    
visitZ(0, 0, 2 ** n)