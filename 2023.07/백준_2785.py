n = int(input())
l = list(map(int, input().split()))

# 정렬
l.sort()
answer = 0      # 소모한 체인 갯수
i = 0
cnt = n - 1     # 연결해야하는 구간

while i < len(l):
    if cnt == 0:
        break
    if l[i] >= cnt:      # l[i]의 갯수가 연결해야하는 구간과 같거나 많으면
        answer += cnt   # 구간의 갯수만큼 체인 사용
        break
    else:   # 구간의 갯수가 l[i] 보다 많거나 작으면 > l[i] 체인 모두 연결하는데 사용
        cnt -= 1        # 연결해야하는 부분 하나 감소
        cnt -= l[i]     # l[i]개 구간 연결
        answer += l[i]  # l[i]개 체인 사용
        i += 1
print(answer)
