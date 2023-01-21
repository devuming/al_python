# 피로도
# 백트래킹 구현 (조합으로도 풀 수 있다고 함)
def solution(k, dungeons):
    global max_answer
    max_answer = 0
    visited = [False] * len(dungeons)

    for i in range(len(dungeons)):
                
        if k >= dungeons[i][0]:
            visited[i] = True       # 방문처리
            dfs(0, dungeons, i, visited, k)
            visited[i] = False       # 방문처리
        
    return max_answer

def dfs(depth, dungeons, v, visited, now_k):
    global max_answer
    depth += 1
    max_answer = max(max_answer, depth)
    now_k -= dungeons[v][1]     # 방문시 피로도 소모

    for i, d in enumerate(dungeons):
        if not visited[i] and now_k >= d[0]:        # 현재 피로도가 최소 필요 소모도 보다 크고, 방문안한 던전일경우
            visited[i] = True
            dfs(depth, dungeons, i, visited, now_k)
            visited[i] = False



print(solution(80, [[80, 20], [50, 40], [30, 10]]))     # 1>3>2 = 3
print()
print(solution(60, [[80, 20], [50, 40], [30, 10]]))     # 3> 2 = 2