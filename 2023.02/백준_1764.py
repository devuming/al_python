# 듣보잡
# 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램
import sys 
n, m = map(int, sys.stdin.readline().rstrip().split())  
cnt_people = {}
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    cnt_people[name] = cnt_people.get(name, 0) + 1

for _ in range(m):
    name = sys.stdin.readline().rstrip()
    cnt_people[name] = cnt_people.get(name, 0) + 1

result = []
for k, v in cnt_people.items():
    if v >= 2:
        result.append(k)

result.sort()
print(len(result))
for i in result:
    print(i)