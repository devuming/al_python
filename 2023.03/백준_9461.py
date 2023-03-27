# 파도반 수열
import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    if n == 1:
        print(1)
        continue
    
    p = [0] * (n + 1)
    p[1] = 1
    p[2] = 1
    for i in range(3, n + 1):
        p[i] = p[i - 2] + p[i - 3]

    print(p[n])