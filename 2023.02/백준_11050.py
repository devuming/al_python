# 이항계수 1
import sys
def bi_co(n, k):
    if k == 0 or k == n:
        return 1
    return bi_co(n-1, k - 1) + bi_co(n-1, k)

n, k = map(int, sys.stdin.readline().rstrip().split())
print(bi_co(n, k))