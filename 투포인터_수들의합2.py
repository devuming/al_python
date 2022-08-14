# 백준_투포인터(슬라이딩 윈도우)_수들의 합  2
# N개의 수로 된 수열 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램
# 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 
# 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
left = 0
sum_value = 0
for right in range(n):
    sum_value += arr[right]
    while sum_value > m:
        sum_value -= arr[left]
        left += 1

    if sum_value == m:
        answer += 1
        
print(answer)
# 4 2
# 1 1 1 1 # =>3

# 10 5
# 1 2 3 4 2 5 3 1 1 2 # => 3