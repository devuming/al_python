# 음계
# 다장조는 c d e f g a b C, 총 8개 음 -> 숫자로바꿔표현
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별
c = [i for i in range(1, 9)]
arr = list(map(int, input().split()))
if arr == c:
    print('ascending')
elif arr == c[::-1]:
    print('descending')
else:
    print('mixed')