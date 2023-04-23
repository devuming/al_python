def solution(people, limit):
    people.sort()
    answer = 0
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            answer += 1
            right -= 1
    return answer

print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) #	3
print(solution([40, 100], 120)) #	2
print(solution([40, 100, 100, 50], 120)) #	3
print(solution([100], 120)) #	1
print(solution([100, 240], 240)) #	2
print(solution([50, 50, 50, 240], 240)) #	3
print(solution([50, 50, 50, 240], 240)) #	3