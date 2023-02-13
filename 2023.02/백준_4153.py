# 백준 4153_직각삼각형
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분
import sys
while True:
    lines = list(map(int, sys.stdin.readline().rstrip().split()))
    lines.sort()
    if lines == [0, 0, 0]:
        break

    if lines[0] ** 2 + lines[1] ** 2 == lines[2] ** 2:
        print("right")
    else:
        print("wrong")