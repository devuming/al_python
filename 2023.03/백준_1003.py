# 피보나치(N)을 호출했을 때 0과 1이 출력되는 횟수 출력
import sys
zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(n):
    if n > len(zero) - 1:
        for i in range(len(zero), n + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])

    print(zero[n], one[n])

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    
    fibonacci(n)