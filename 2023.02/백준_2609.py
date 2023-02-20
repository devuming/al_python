# 백준 2609_최대공약수와 최소공배수
import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

def gcd(a, b):
    while b > 0:
        a = a % b
        a, b = b, a % b
    return a

def lcd(a, b):
    return (a * b) // gcd(a, b)

print(gcd(a, b))
print(lcd(a, b))
