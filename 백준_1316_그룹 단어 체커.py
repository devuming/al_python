# 백준_1316_그룹 단어 체커
# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.
n = int(input())
count = 0

for _ in range(n):
    value = input()
    dic = {}
    count += 1
    
    for i, v in enumerate(value):
        if dic.get(v, 0) != 0 and value[i-1] != v:
            count -= 1
            break
        dic[v] = dic.get(v, 0) + 1

print(count)