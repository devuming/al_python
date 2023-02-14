# 나이순 정렬
# 안정정렬
import sys
n = int(sys.stdin.readline().rstrip())
members = []
for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    members.append((int(age), name))    # 나이 int 변환 필수
    
members.sort(key=lambda x:x[0])
for member in members:
    print(member[0], member[1])