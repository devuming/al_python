# 백준_전자레인지
# 3개의 시간조절용 버튼 A B C가 달린 전자레인지가 있다. 
# # 각 버튼마다 A, B, C에 지정된 시간은 각각 5분, 1분, 10초, 해당 버튼을 한번 누를 때마다 그 시간이 동작시간에 더해진다

# 냉동음식마다 전자레인지로 요리해야할 시간 T가 초단위로 표시되어 있다. 우리는 A, B, C 3개의 버튼을 적절히 눌러서 그 시간의 합이 정확히 T초가 되도록 해야 한다. 
# 단 버튼 A, B, C를 누른 횟수의 합은 항상 최소가 되어야 한다.

# 만일 요리시간이 100초라고 하면(T=100) B를 1번, C는 4번 누르면 된다. 이와 다르게 C를 10번 눌러도 100초가 되지만 이 경우 10번은 최소 횟수가 아니기 때문이 답이 될 수 없다. 
t = int(input())        # 주어진 시간 (초)

btn = [60 * 5, 60, 10]
answer = [0] * 3

for i in range(3):
    while t >= 0 and t >= btn[i]:
        t -= btn[i]
        answer[i] += 1

if t == 0:
    print(f"{answer[0]} {answer[1]} {answer[2]}")
else:
    print('-1')