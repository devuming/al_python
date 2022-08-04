# DFSBFS_숨바꼭질
# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에, 동생은 점 K(0 ≤ K ≤ 100,000)에
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 입력 : 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
# 출력 : 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
from collections import deque

n, k = map(int, input().split(' '))
queue = deque()
second = [-1] * 100001
second[n] = 0
queue.append((n, 0))     # n 부터 탐색 시작

while queue:
    now, sec = queue.popleft()
    sec += 1

    if now == k:
        break

    if now + 1 <= 100000 and second[now + 1] == -1:
        second[now + 1] = sec
        queue.append((now + 1, sec))
    if now - 1 > 0 and second[now - 1] == -1:
        second[now - 1] = sec
        queue.append((now - 1, sec))
    if now * 2 <= 100000 and second[now * 2] == -1:
        second[now * 2] = sec
        queue.append((now * 2, sec))
    
print(second[k])