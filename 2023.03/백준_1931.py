# 회의실 배정 
import sys
n = int(sys.stdin.readline().rstrip())
times = []
for _ in range(n): 
    s, e = map(int, sys.stdin.readline().rstrip().split())
    times.append((s, e))

# 빨리 끝나는 회의 순대로 해야 많은 회의를 할 수 있음 
# > 정렬 (1. 일찍 끝나는 순, 2. 일찍 시작하는 순)
times.sort(key=lambda x:(x[1], x[0]))
count = 1
end_time = times[0][1]

for i in range(1, n):
    if times[i][0] >= end_time:  # 끝나는 시간 이후의 회의일 경우
        count += 1
        end_time = times[i][1]

print(count)