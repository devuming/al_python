# 그리디_문자열 뒤집기
# 0과 1로만 이루어진 문자열을 모든 숫자가 같도록 만들기 위해
# 뒤집기 위한 행동의 최소 횟수
s = input()

count_0 = 0 # 0으로 바뀌는 경우
count_1 = 0 # 1로 바뀌는 경우

if s[0] == '1':
    count_0 += 1
else:
    count_1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '1':
            count_0 += 1
        else :
            count_1 += 1

if count_0 < count_1:
    print(count_0)
else:
    print(count_1)
