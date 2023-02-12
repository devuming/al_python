# 백준 2839 _ 설탕배달
# 3킬로그램 5킬로그램 봉지가 있을 때, 최대한 적은 봉지를 들고 가려고 한다
# 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램
import sys
n = int(sys.stdin.readline().rstrip())

if n % 5 == 0:
    print(n // 5)
else:
    answer = 0
    while n > 0:
        if n % 5 == 0:
            answer += n // 5
            n = n % 5
            break
        elif n < 3:
            break
        
        n -= 3
        answer += 1
    
    if n > 0:
        print(-1)
    else:
        print(answer)
            
