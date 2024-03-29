# 개미전사
# 식량창고 털기
# 일직선상에 존재하는 식량창고 중에서 최소 한칸 이상 떨어진 식량창고만 약탈할 수 있다고 할때
# 얻을 수 있는 ㅅ긱량의 최댓값
# 입력 : 식량창고 갯수 N, 각 식량 창고에 저장된 식량의 갯수 K
# 출력 : 개미전사가 얻을 수 있는 식량의 최대값

n = int(input())
k = list(map(int, input().split()))     # 각 창고의 식량 갯수 : 배열

d = [0] * 1000
d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i-2] + k[i], d[i - 1])

# 최댓값 출력
print(d[n - 1])