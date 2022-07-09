# 곱하기 혹은 더하기
# 문자열 s가 주어졌을 때, * 혹은 + 를 사용해 만들 수 있는 가장 큰 수를 구하는 프로그램
# 왼쪽에서부터 순서대로 이루어짐
def solution(s):
    nums = list(map(int, s))
    result = 0

    for num in nums:
        if result <= 1 or num <= 1:        # num이 0이거나 1이면 더하는게 더 큰수를 만들 수 있음
            result += num
        else:
            result *= num
    
    return result

print(solution('02984'))    # 576
print(solution('567'))      # 210
print(solution('111'))      # 3
