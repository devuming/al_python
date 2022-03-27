# 퇴사문제
# 오늘부터 N + 1일째 되는 날 퇴사하기 위해 남은 N일 동안 최대한 많은 상담을 하려고함
# 상담을 완료하는 데 걸리는 기간 T[i]와 상담을 했을 때 받을 수 있는 금액 P[i] 로 이루어짐

n = int(input())
t = [] * (n + 1)
p = [] * (n + 1)

for i in range(n + 1) :
    t[i], p[i] = map(int, input().split())

print(t)
print(p)