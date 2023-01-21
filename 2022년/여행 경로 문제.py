# 여행 경로 문제
def solution(tickets):      # 항공권
    answer = []     # 방문하는 공항 경로
    
    stack = []      # 도착지 공항 
    tickets.sort(key=lambda x:x[1])
    print(tickets)
    # for i in tickets:
        
    
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))