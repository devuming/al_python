n, b = input().split()
b = int(b)

answer = 0
for i, num in enumerate(n):
    c = (len(n) - 1) - i
    if num.isalpha():
        tmp_num = 10 + (ord(num) - ord('A'))
    else:
        tmp_num = int(num)
    
    tmp_num = tmp_num * (b ** c)
    answer += tmp_num
print(answer)