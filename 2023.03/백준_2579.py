import sys
n = int(sys.stdin.readline().rstrip())
answer = [0] * (n)
scores = []

for _ in range(n):
    scores.append(int(sys.stdin.readline().rstrip()))

if n == 1:
    print(scores[0])
elif n == 2:
    print(max(scores[0] + scores[1], scores[1]))
else:
    answer[0] = scores[0]
    answer[1] = max(scores[0] + scores[1], scores[1])   # 첫번째 계단을 밟고 두번째 계단을 밟거나/두번째 계단만 밟거나
    answer[2] = max(scores[0], scores[1]) + scores[2]

    for i in range(3, n):
        answer[i] = max(answer[i - 2] + scores[i], scores[i - 1] + scores[i] + answer[i - 3])

    print(answer[n - 1])