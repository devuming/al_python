import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
flowers = []

for _ in range(n):
    from_m, from_d, to_m, to_d = map(int, sys.stdin.readline().rstrip().split())

    flowers.append((from_m * 100 + from_d, to_m * 100 + to_d))
flowers.sort(key=lambda x:(x[0], x[1]))
flowers = deque(flowers)

count = 0       # 선택한 꽃의 갯수
end = 301       # 마지막 꽃의 지는 날짜

while flowers:
    if end >= 1201 or end < flowers[0][0]:
        break
    temp_end = -1
    # 모든 꽃들과 비교해서 현재 꽃보다 일찍 피고 늦게 지는 꽃을 찾는다.
    for _ in range(len(flowers)):
        if flowers[0][0] > end:   # 시작일자가 target보다 작은 경우
            break
        if temp_end <= flowers[0][1]:
            temp_end = flowers[0][1]
        flowers.popleft()
    # 마지막 지는 꽃 end_date 업데이트
    end = temp_end
    count += 1
    
if end < 1201:
    print(0)
else:
    print(count)