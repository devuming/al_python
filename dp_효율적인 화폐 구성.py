# 효율적인 화폐 구성
# N가지 종류의 화폐
# 화폐의 개수를 최소한으로 이용해 가치의 합이 M 원이 되도록
# 구성이 같고 순서만 다른 경우는 같은 경우
# 입력 : N, M (1 <= N <= 100, 1 <= M <= 10000)
#        N개의 줄 - 화폐의 가치 (10,000 보다 작거나 같은 자연수)
# 출력 : 경우의 수 X, 불가능 할 경우 -1

n, m = map(int, input().split())
array = []         # 화폐의 가치 배열
for i in range(0, n):
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in range(1, m + 1):
    for k in array:
        if i - k >= 0:
            d[i] = min(d[i], d[i - k] + 1)  # 화폐 k를 추가한 경우의 수 + 1 와 비교

if d[m] == 10001:
    print('-1')
else:
    print(d[m])