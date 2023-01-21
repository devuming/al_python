# 그리디_ATM
# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램
n = int(input())
p = list(map(int, input().split()))

# 1. 걸리는 시간 순으로 정렬 (오름차순)
p.sort()

# 2. 돈 인출하는 데 걸리는 시간 계산
answer = 0
previous = 0
for i in range(n):
    previous += p[i]
    answer += previous

print(answer)