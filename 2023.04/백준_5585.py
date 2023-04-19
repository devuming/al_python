# 입력 : 지불할 돈
# 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
# 1000엔 지폐를 한장 낸다.
n = int(input())
left = 1000 - n
money = [500, 100, 50, 10, 5, 1]
count = 0
while left > 0:
    for m in money:
        if left >= m:
            left -= m
            count += 1
            break
print(count)