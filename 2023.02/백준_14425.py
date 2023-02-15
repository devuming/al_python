# 문자열 집합
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
dic_s = {}
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    dic_s[s] = dic_s.get(s, 0) + 1

count = 0
for _ in range(m):
    chk_s = sys.stdin.readline().rstrip()
    if dic_s.get(chk_s, 0) > 0:
        count += 1
print(count)