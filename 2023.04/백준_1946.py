import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    score = []
    for _ in range(n):
        score.append(list(map(int, sys.stdin.readline().rstrip().split())))
    score.sort(key=lambda x:x[0])
    temp = score[0][1]  # 서류 1등의 면접 점수
    count = 1
    for i in range(n):
        if temp > score[i][1]:  # 숫자가 작을 수록 등수가 높은 것
            count += 1
            temp = score[i][1]

    print(count)