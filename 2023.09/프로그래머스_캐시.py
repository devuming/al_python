from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    for i, city in enumerate(cities):
        if cacheSize == 0:
            answer += 5
        else:
            if city.upper() in cache:
                # cache hit
                answer += 1
                for i in range(cacheSize):
                    if cache[i] == city.upper():
                        del cache[i]
                        break
            else:
                # cache miss
                if len(cache) >= cacheSize:
                    cache.popleft()
                answer += 5

            cache.append(city.upper())
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork",
      "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
      "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25
