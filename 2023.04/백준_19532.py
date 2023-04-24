import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().rstrip().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):#2000 * 2000 = 4,000,000
        if (a * x + b * y) == c and (d * x + e * y) == f:
            print(x, y)
            exit(0)