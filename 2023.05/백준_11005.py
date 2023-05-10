n, b = map(int, input().split())
answer = ''

while n > 0:
    tmp_num = n % b
    if tmp_num >= 10:
        tmp_num = chr(ord('A') + tmp_num - 10)
    answer = str(tmp_num) + answer
    n //= b
print(answer)