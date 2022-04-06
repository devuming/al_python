# 더 맵게 
import heapq

def solution(scoville, K):      # 음식의 스코빌 지수를 담은 배열, 기준 스코빌 지수
    answer = 0                  # 모든 음식의 스코빌 지수를 K이상으로 만들기 위한 섞는 횟수 최소값
    
    heapq.heapify(scoville)     # 스코빌 지수를 힙으로 변환    

    while scoville[0] < K and len(scoville) > 1:
        # 섞을 음식 힙에서 삭제하면서 스코빌 지수 가져옴
        min_scoville = heapq.heappop(scoville)  # 가장 맵지 않은 음식의 스코빌 지수
        sec_scoville = heapq.heappop(scoville)  # 두번째 스코빌 지수
        
        if min_scoville >= K and sec_scoville >= K:   # 둘다 이미 K 이상이면 섞지 않음
            break

        # 섞은 음식의 스코빌 지수 삽입
        mix_scoville = min_scoville + (sec_scoville * 2)    # 가장 맵지 않은 음식 + (두번째 스코빌 지수 * 2)
        heapq.heappush(scoville, mix_scoville)      # 새로운 음식 추가

        answer += 1                                 # 섞은 횟수 증가   
    
    return answer if scoville[0] >= K else -1

# print(solution([1, 1, 1, 1, 1, 1, 1, 1], 8))        # 6
# print(solution([1000000, 1], 999999))                # 1
# print(solution([1000000, 1], 1000000))               # 1
# print(solution([1000000, 1], 10000000))               # -1


print(solution([1, 2], 5))               # 1