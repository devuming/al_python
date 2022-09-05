# 백준_2588_곱셈
a = input()
b = input()
result = 0

for i in range(2, -1, -1):
    c = 0
    for j in range(2, -1, -1):
        c += int(a[j]) * int(b[i]) * (10 ** (2 - j))
    print(c)
    result += c * (10 ** (2 - i))

print(result)