# 좌표 압축
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# -> 정렬 후 순서 
import sys
n = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
ranks = list(set(nums))
ranks.sort()
dic_score = {rank:i for i, rank in enumerate(ranks)}

for num in nums:
    print(dic_score[num], end=' ')