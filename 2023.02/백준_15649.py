# 백준 15649_N과 M (1) : 백트래킹
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열

global n, m
n, m = map(int, input().split())

def back(arr, visited):
    if len(arr) == m:
        for i in arr:
            print(i, end=' ')
        print()
    else:
        for j in range(1, n + 1):
            # if j not in arr: -> visited 배열 사용 30ms 정도 단축?
            if not visited[j]:
                arr.append(j)
                visited[j] = True
                back(arr, visited)
                arr.pop()
                visited[j] = False

for i in range(1, n + 1):
    arr = [i]
    visited = [False] * (n + 1)
    visited[i] = True   # 사용 여부 체크
    back(arr, visited)