# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수
# 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT
def solution(a, b):
    answer = ''
    dayweek = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    daymonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30]    
    day_cnt = 0
    
    for i in range(a - 1):
        day_cnt += daymonth[i - 1]   
    day_cnt += b
    
    print(day_cnt)
    d_w = day_cnt % 7
    
    return dayweek[d_w - 1]  

print(solution(1, 10))
print(solution(5, 24))
# print(solution(2, 10))
# print(solution(3, 10))
# print(solution(4, 10))
# print(solution(5, 10))
# print(solution(6, 10))
# print(solution(7, 10))
# print(solution(8, 10))
# print(solution(9, 10))
# print(solution(10, 10))
# print(solution(11, 10))
# print(solution(12, 10))