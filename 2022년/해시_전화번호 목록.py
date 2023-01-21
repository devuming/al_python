# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요
def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if phone_book[i] == phone_book[j]:
                continue
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                answer = False
                break
    
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))