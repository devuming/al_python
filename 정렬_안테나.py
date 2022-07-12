# 정렬_안테나
# 안테나에서 모든 집까지의 거리의 총합이 최소가 되는 안테나의 위치를 구하는 알고리즘
# 안테나는 집이 위치한 곳에만 설치할 수 있음
n = int(input())        # 집의 수
position = list(map(int, input().split()))      # 집의 위치

# 위치 순으로 정렬 (오름차순)
position.sort()

# 중간에 안테나를 설치하면 모든 집까지의 거리의 총합이 최소가 됨
print(position[(n-1) // 2])