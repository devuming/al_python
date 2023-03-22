import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
pass_dic = {}

for _ in range(n):
    site, password = sys.stdin.readline().rstrip().split()
    pass_dic[site] = password
for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(pass_dic[site])