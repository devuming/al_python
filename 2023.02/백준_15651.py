# 백준 15650 N과 M(3)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 1부터 N까지 자연수 중에서 M개를 고른 수열, 같은 수를 여러 번 골라도 된다.
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

n, m = map(int, input().split())

def back(arr):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    else:
        for j in range(1, n + 1):
            arr.append(j)
            back(arr)
            arr.pop()

for i in range(1, n + 1):
    arr = [i]
    back(arr)