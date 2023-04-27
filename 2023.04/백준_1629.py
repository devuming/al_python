import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())

def divide_conquer(a, b, c):
    if b == 1 :
        return a % c
    temp = divide_conquer(a, b // 2, c)
    if b % 2 == 0:
        return temp ** 2 % c
    else:
        return temp ** 2 * a % c

print(divide_conquer(a, b, c))