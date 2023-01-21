# 그리디_잃어버린괄호
# 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램
exp = input()

# 마이너스 기호를 만날 때, 다음 마이너스까지 모두 더해 한번에 빼면 최소값
arr = exp.split('-')
answer = 0

for i in arr[0].split('+'):
    answer += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)