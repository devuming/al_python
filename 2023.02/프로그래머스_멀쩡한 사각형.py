# 최대공약수 구하기
def gcd(x, y):
    while y : 
        x , y = y, x % y
    
    return x

def solution(w,h):
    answer = 0

    # 대각선으로 사용할 수 없게된 정사각형 갯수 = 가로 + 세로 - 최대공약수
    answer = (w * h) - (w + h - gcd(w, h)) # 원래 갯수 - 대각선으로 사용할 수 없게된 정사각형 갯수
    
    return answer

print(solution(8, 12))      # 80
print(solution(2, 3))       # 2