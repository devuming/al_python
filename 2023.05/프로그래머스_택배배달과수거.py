def solution(cap, n, deliveries, pickups):
    answer = 0
    cnt_d, cnt_p = 0, 0
    for i in range(n - 1, -1, -1):
        cnt_d += deliveries[i]
        cnt_p += pickups[i]     # 택배수, 수거택배수
        
        while cnt_d > 0 or cnt_p > 0:
            cnt_d -= cap
            cnt_p -= cap
            answer += (i + 1) * 2

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])) # 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])) # 30