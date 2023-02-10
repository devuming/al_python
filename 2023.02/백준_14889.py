# 백준 14889_스타트와 링크
# N/2 명으로 이루어진 스타트팀과 링크팀이 축구함
# 두 팀의 능력치의 차이를 최소값 구하기
import sys

result = 10e9
def dfs(idx, score1):
    global result
    if len(a_team) == n // 2:
        score2 = 0
        b_team = [i for i in range(n) if i not in a_team]
        
        for i, b in enumerate(b_team):
            for j in range(i + 1, n//2):
                score2 += s[b][b_team[j]] + s[b_team[j]][b]
        
        result = min(result, abs(score1 - score2))

        return

    for i in range(idx + 1, n): # 0 ~ n - 1  까지의 사람과 모두
        temp = 0
        for j in a_team:
            temp += s[i][j] + s[j][i]  # a 팀에 속한 모든 사람들과의 능력치 계산

        a_team.append(i)
        dfs(i, score1 + temp)
        a_team.pop()

n = int(sys.stdin.readline().rstrip())
s = []  # s[i][j] 는 i번째 사람과 j번째 사람이 같은 팀일때 팀에 더해지는 능력치
a_team = []
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().rstrip().split())))

a_team.append(0)
dfs(0, 0)
print(result)