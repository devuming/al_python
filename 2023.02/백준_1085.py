# 백준 1085_직사각형에서 탈출
# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행
# 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
# 직사각형의 경계선까지 가는 거리의 최솟값
import sys
x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
answer = min(x, y, w - x, h - y)
print(answer)