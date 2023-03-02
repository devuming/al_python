import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
d_broken = {str(k):1 for k in range(10)} # 고장난 키 체크용
broken = list(sys.stdin.readline().rstrip().split())
for b in broken:
    d_broken[b] -= 1

# 현재 채널과의 차이 : +- 로 이동
min_count = abs(n - 100)

for i in range(1000001):
    num = str(i)

    for j in range(len(num)):
        if d_broken[num[j]] == 0:
            break
        # 고장난 번호 빼고 만들 수 있는 숫자인 경우, 해당 채널 번호에서 +- 로 이동한 경우 횟수 최소값 비교
        if j == len(num) - 1:
            min_count = min(min_count, len(num) + abs(i - n))

print(min_count)