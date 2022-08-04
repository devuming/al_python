# 그리디_볼링공 고르기_답지
n, m = map(int, input().split(' '))
arr = [0] * 11

ball = list(map(int, input().split(' ')))
for i in ball:
    arr[i] += 1     # 무게별 볼링공 갯수 count

# 서로 다른 무게의 볼링공을 두 사람이 고를 때
# 경우의 수 계산
result = 0
for i in range(1, m + 1):   # 무게 1 ~ M 까지의 경우의 수
    n -= arr[i]             # a가 무게가 i 인 볼링공을 골랐을 때, b가 볼링공을 고를 수 있는 수
    result += arr[i] * n    # a가 무게 i인 공을 고를 수 있는 경우의 수 * b 가 나머지 볼링공을 고를 수 있는 경우의 수

print(result)