# 가장큰수 2회차
def solution(number):
    number.sort(key=lambda x : (str(x) * 4)[:4], reverse=True)     # 오름차순 정렬
    answer = ''.join(list(map(str, number)))
    return answer if int(answer) != 0 else "0"

print(solution([6, 10, 2])) #	"6210"
print(solution([3, 30, 34, 5, 9])) #	"9534330"
print(solution([3, 999, 34, 5, 9])) #	"99995343"
print(solution([3, 999, 34, 5, 0])) #	"99953430"
print(solution([121, 11, 99, 7, 3])) #	[9900,7000,3000,1210,1100]"997312111"
print(solution([0, 0, 9]))          # "900"
print(solution([0, 0, 0]))          # "0"
print(solution([1000,1000,1000]))          # 100010001000
print(solution([1000,1000,1000, 0]))          # 1000100010000
print(solution([999,1000,1000, 0]))          # 999100010000