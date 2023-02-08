# 백준 15650 N과 M(4)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 같은 수를 여러 번 골라도 된다. & 고른 수열은 비내림차순이어야 한다
# 중복되는 수열을 여러 번 출력하면 안되며, 사전 순으로 증가하는 순서로 출력
n, m = map(int, input().split())

def back(arr, i):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    else:
        for j in range(i, n + 1):
            arr.append(j)
            back(arr, j)
            arr.pop()

for i in range(1, n + 1):
    arr = [i]
    back(arr, i)