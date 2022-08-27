# 백준_알고리즘 수업_피보나치 수
# 입력 : 첫째 줄에 n(5 ≤ n ≤ 40)이 주어진다.
# 출력 : 코드1 코드2 실행 횟수를 한 줄에 출력한다.

def fib(n):
    count = 0
    if n == 1 or n == 2:
        count = 1
    else :
        count += (fib(n - 1) + fib(n - 2))
    return count


def fibonacci(n):
    count = 0
    f = [0] * (n + 1)
    f[1] = f[2] = 1

    for i in range(3, n + 1):
        count += 1
        f[i] = f[i - 1] + f[i - 2];  # 코드2
        
    return count
    
import sys
n = int(sys.stdin.readline().rstrip())

count_1 = fib(n)
count_2 = fibonacci(n)

print(count_1, count_2)