# 백준 10807 개수세기
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())

count = 0
for num in nums:
    if num == v:
        count += 1

print(count)