import math
while True:
    n = int(input())
    if n == -1:
        break
    answer = []
    total = 0
    
    for i in range(1, n):
        if n % i == 0:
            answer.append(str(i))
            total += i
            
    if total == n:
        print(f'{n} = {" + ".join(answer)}')
    else:
        print(f'{n} is NOT perfect.')