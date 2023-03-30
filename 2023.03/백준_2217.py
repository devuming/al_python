import sys
n = int(sys.stdin.readline().rstrip())
ropes=[]
max_weight = 0
for _ in range(n):
    ropes.append(int(sys.stdin.readline().rstrip()))
ropes.sort()

answer = 0
for i in range(n - 1, -1, -1):
    temp = ropes[i] * (n - i)
    if temp > answer:
        answer = temp
print(answer)