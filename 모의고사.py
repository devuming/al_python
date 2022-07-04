def solution(answers):      # 정답 배열
    answer = []
    ans_a = [1, 2, 3, 4, 5]
    ans_b = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if ans == ans_a[i % len(ans_a)]:
            cnt[0] += 1
        if ans == ans_b[i % len(ans_b)]:
            cnt[1] += 1
        if ans == ans_c[i % len(ans_c)]:
            cnt[2] += 1
                
    for i, c in enumerate(cnt):        
        if c == max(cnt):
            answer.append(i + 1)
    
    return answer       # 가장 많은 문제를 맞춘 사람

print(solution([1,2,3,4,5]))    #	[1]
print(solution([1,3,2,4,2]))    #	[1,2,3]