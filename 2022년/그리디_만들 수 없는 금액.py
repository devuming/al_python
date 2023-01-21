# 그리디 - 만들 수 없는 금액
# N개의 동전으로 만들 수 없는 양의 정수 금액 중 최소값을 구하는 프로그램
# N개의 동전의 각각의 단위가 주어짐
n = int(input())
coin = list(map(int, input().split(' ')))

# 1. 동전 단위 오름차순 정렬
coin.sort()

# 2. 동전들로 만들 수 있는 금액 구하기 1~target-1 까지
# target 이 구할 수 없는 최소 금액 임
target = 1
for i in coin:
    if target < i:
        break
    target += i     # 1 ~ target - 1 까지는 만들 수 있는 금액

print(target)