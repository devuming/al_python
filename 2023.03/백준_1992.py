# 쿼드 트리
import sys
n = int(sys.stdin.readline().rstrip())
video = []
for _ in range(n):
    video.append(list(sys.stdin.readline().rstrip()))

def divideVideo(x, y, n):
    if n == 1:
        print(video[x][y], end='')
        return
    
    # 모두 같은 수인지 확인
    divideFlag = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if video[i][j] != video[x][y]:
                divideFlag = True  # 다른 수 체크
                break
        if divideFlag:
            break

    if not divideFlag: 
        print(video[x][y], end='')  # video[x][y]로 압축
        return
    
    # 4개 영역 : 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
    size = n // 2
    print("(", end='')
    divideVideo(x, y, size)
    divideVideo(x, y + size, size)
    divideVideo(x + size, y, size)
    divideVideo(x + size, y + size, size)
    print(")", end='')

divideVideo(0, 0, n)