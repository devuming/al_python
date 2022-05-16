# 스택/큐 > 기능개발
def solution(progresses, speeds): # 먼저 배포되어야 하는 순서대로 작업의 진도 progresses, 각 작업의 개발 속도 speeds
    answer = []

    # 배포되어야하는 순서대로 배포되어야함, 뒤에꺼가 먼저 완료되더라도 앞에 꺼가 완료되어야 배포 가능
    work = []
    for p in progresses:
        work.append(p)

    while work:
        for i in range(len(work)):
            if work[i]  < 100:
                work[i] = work[i] + speeds[i] if work[i] + speeds[i] < 100 else 100   # 진도 증가
        
        cnt = 0             # 배포되는 기능 횟수

        if work[0] == 100:  # 완료되면
            while work and work[0] == 100:
                cnt += 1        # 배포되는 기능 횟수 증가
                work.pop(0)     # 먼저 들어온것 부터 배포  
                speeds.pop(0)

            answer.append(cnt)

    return answer   # 각 배포마다 몇 개의 기능이 배포되는지

print(solution([93, 30, 55],	[1, 30, 5] ))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))