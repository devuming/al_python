def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1].split(':')[0]) * 60 + int(x[1].split(':')[1]), int(x[2])], plans), key=lambda x: -x[1])
    print(plans)
    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]]) # 과제 종료 시간 저장
        print(lst)
    lst.sort()

    return list(map(lambda x: x[1], lst))

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))   #	["korean", "english", "math"]
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))#["science", "history", "computer", "music"]
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))   #["bbb", "ccc", "aaa"])