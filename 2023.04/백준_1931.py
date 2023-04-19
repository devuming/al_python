import sys
n = int(sys.stdin.readline().rstrip())
time = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    time.append((start, end))
time.sort(key=lambda x : (x[1], x[0]))
count = 1
pre_end = time[0][1]
for i in range(1, len(time)):
    if time[i][0] >= pre_end:
        count += 1
        pre_end = time[i][1]

print(count)