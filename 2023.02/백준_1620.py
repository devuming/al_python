# 나는냐 포켓몬 마스터 이다솜
import sys 
n, m = map(int, sys.stdin.readline().rstrip().split())
mon_idx = {}
mon_name = {}
for i in range(n):
    name = sys.stdin.readline().rstrip()
    mon_idx[i + 1] = name
    mon_name[name] = i + 1

# 문제 갯수 = m
for _ in range(m):
    # 문제 입력받음
    q = sys.stdin.readline().rstrip()
    if q.isalpha():
        # 숫자 출력
        print(mon_name[q])
    else:
        # 문자 출력
        print(mon_idx[int(q)])