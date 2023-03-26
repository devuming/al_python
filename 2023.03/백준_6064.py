import sys

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return m * n / gcd(a, b)

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    max_year = lcm(m, n)
    
    while True:
        if x > max_year or (x - 1) % n + 1 == y:
            break
        x += m
    if x > max_year:
        print(-1)
    else:
        print(x)
    