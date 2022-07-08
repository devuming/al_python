from collections import deque

def solution(priorities, location):     # 중요도, 요청한 문서의 위치
    doc = deque()        # 문서 스택
    print_list = []
    
    for i, p in enumerate(priorities):     
        doc.append((i, p))

    answer = 0
        
    while doc:        
        front = doc.popleft()
        flag = False

        for d in doc:
            if front[1] < d[1]:         # 대기목록의 문서에 우선순위 높은 문서가 있는지 확인
                flag = True   
                break
        if flag:
            doc.append(front)       # (인덱스, 우선순위)
        else:            
            print_list.append(front)
            answer += 1

        print(doc)

    for i, p in enumerate(print_list):
        if p[0] == location:
            return i + 1  

print(solution([2, 1, 3, 2], 2))        # 1
print(solution([1, 1, 9, 1, 1, 1], 0))