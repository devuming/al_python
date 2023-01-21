# Dijkstra's Algorithm
# 가중치가 있는 방향성 그래프에서 한 특정 정점에서 다른 모든 정점으로 가는 최단 경로를 구하는 문제
# 시작점 : V1
def dijkstra(n, W, F):
    F = []                  # 엣지 집합 F 초기화
    touch = [0, 0, ]        # Vi로 거쳐가는 정점 (i는 배열 인덱스, V0/V1 : 사용 안하는 인덱스)
    length = [0, 0, ]       # Vi로 가는 경로 길이 (i는 배열 인덱스, V0/V1 : 사용 안하는 인덱스)

    # touch : 거쳐가는 정점 V1으로 , length : 정점 V1에서 Vi로 가는 길이 초기화
    for i in range(2, n + 1):
        touch.append(1)             # v1 거쳐 간다고 표시
        length.append(W[0][i - 1])  # 정점 v1에서 vi로 가는 경로

    for _ in range(n-1):        # n - 1 정점들 Y에 추가하기 위한 Loop
        min = 999999            # infinite 값으로 최소 길이 초기화

        for i in range(2, n + 1):                   # v2부터 vn 중
            if 0 <= length[i] and length[i] < min:  # 최단 거리의 정점 선택
                min = length[i]
                vnear = i                           # vnear : 최단거리 정점 index

        # Solution Set F에 최단 거리 Edge 추가
        tindex = touch[vnear]                              # touch[vnear]에 저장된 정점에서 vnear 정점으로 가는 엣지,
        e = (W[tindex-1][vnear-1], touch[vnear], vnear)    # Edge Format : (가중치, 출발정점, 도착정점)
        F.append(e)                                        # Solution Set F 에 엣지 추가

        # Y에 속하지 못한 정점 최단 경로 길이 갱신 & touch에 vnear
        for i in range(2, n + 1):
            if length[vnear] + W[vnear-1][i-1] < length[i]: # vnear 정점을 거쳐서 Vi로 가는 경로가 length가 저장하고 있는 길이보다 짧으면
                length[i] = length[vnear] + W[vnear-1][i-1] # length에 저장된 최단 길이 갱신 : v1 -> vnear 정점 -> vi 경로
                touch[i] = vnear                            # v1에서 vi로 갈때 vnear 정점 거치도록 touch 갱신

        length[vnear] = -1      # 선택된 정점은 -1로 set (다시 지나가지 않기 위해)

    return F        # 엣지 집합 F 리턴

# ==== main =====
F = []                                      # 최단 경로 엣지 배열

# Figure 4.8 Test
# 그래프 W 배열 (인덱스 0부터 시작)
print('---- Figure 4.8 ----')
W = [[0, 7, 4, 6, 1],                       # V1 -> Vn 연결 경로 (가중치)
     [999999, 0, 999999, 999999, 999999],   # V2 -> Vn
     [999999, 2, 0, 5, 99999],              # V3 -> Vn
     [999999, 3, 99999, 0, 999999],         # V4 -> Vn
     [999999, 999999, 999999, 1, 0]         # V5 -> Vn
     ]

F = dijkstra(5, W, F)
print("집합 F : ", F)

print()

# 자작 데이터 Test
print('---- 자작 입력 데이터 ----')
W = [[0, 3, 7, 5, 999999],              # V1 -> Vn 연결 경로 (가중치)
     [999999, 0, 2, 1, 999999],         # V2 -> Vn
     [999999, 999999, 0, 999999, 1],    # V3 -> Vn
     [999999, 999999, 999999, 0, 4],    # V4 -> Vn
     [3, 999999, 999999, 999999, 0] # V5 -> Vn
     ]

F = dijkstra(5, W, F)
print("집합 F : ", F)
