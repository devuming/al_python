import sys
n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or '0' not in n:
    print(-1)
else:
    print(''.join(n))
# 왜 모든 자릿수의 합이 3이면 30의 배수가 될 수 있는가?
# 배수 판정법 
# 3의 배수 판정법 : 모든 자시릐 수의 합이 3의 배수
