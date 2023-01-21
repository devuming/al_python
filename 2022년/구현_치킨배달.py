# 치킨 배달
from itertools import combinations

INF = 99999
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            houses.append((i, j))
        elif matrix[i][j] == 2:
            chickens.append((i, j))

# 최대 M개를 골라 도시의 치킨거리(모든 치킨 거리의 합)가 가장 작은 경우 찾기
# m개의 조합
chick_combi = list(combinations(chickens, m))

result = INF

for chick in chick_combi:
    distance_sum = 0
    
    for house in houses:
        distance = INF
        for c in chick:
            distance = min(distance, abs(c[0] - house[0]) + abs(c[1] - house[1]))
            
        distance_sum += distance

    if distance_sum < result:
        result = distance_sum

print(result)

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2
##### 5

# 5 2 
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0 
# 2 0 0 1 1
# 2 2 0 1 2
##### 10

# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
##### 11