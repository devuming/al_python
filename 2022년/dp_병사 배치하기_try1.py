# dp_병사 배치하기
# 무작위로 나열되어있는 N명의 병사에서 특정 위치의 병사를 열외시켜 내림차순으로 배치할때
# 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야하는 병사의 수
n = int(input())
arr = list(map(int, input().split(' ')))
stk = []

i = 0
stk.append(arr[i])

while stk:
    i += 1
    if i == n:
        break

    # 남아있는 병사의 수가 최대가 되어야함
    if arr[i] > stk[-1]:
        stk.pop()

    stk.append(arr[i])

print(n - len(stk))