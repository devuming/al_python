# 셀프 넘버
d = list(range(1, 10001))
l = []

for i in range(1, 10001):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result <= 10000:
        l.append(result)

for i in d:
    if i not in l:
        print(i)

