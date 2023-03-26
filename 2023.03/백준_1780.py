# 종이의 갯수
import sys
n = int(sys.stdin.readline().rstrip())
paper = []
for _ in range(n):
    paper.append(list(sys.stdin.readline().rstrip().split()))
cnt = {'-1':0, '0':0, '1':0}

def cutPaper(x, y, n):
    if n == 1:
        cnt[paper[x][y]] += 1
        return
    
    # 모두 같은 수인지 확인
    paperNum = paper[x][y]
    cutFlag = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != paperNum:
                cutFlag = True  # 다른 수가 있는 경우 종이 자르기
                break
        if cutFlag:
            break

    if not cutFlag: 
        cnt[paperNum] += 1  # 해당 숫자의 종이 수 증가
        return
    
    # 9개로 자르기 : cutFlag가 바꼈다면 종이가 같은 수가 아님
    paperSize = n // 3
    for i in range(0, 3):
        for j in range(0, 3):
            cutPaper(x + (i * paperSize), y + (j * paperSize), paperSize)

cutPaper(0, 0, n)
# 결과 출력
print(cnt['-1'])
print(cnt['0'])
print(cnt['1'])
