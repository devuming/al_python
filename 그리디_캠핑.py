# 백준_그리디_캠핑
# 캠핑장은 연속하는 20일 중 10일동안만 사용할 수 있습니다.
# 강산이는 이제 막 28일 휴가를 시작했다. 이번 휴가 기간 동안 강산이는 캠핑장을 며칠동안 사용할 수 있을까?
# 강산이는 조금 더 일반화해서 문제를 풀려고 한다. 
# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다. 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)
answers = []

while True:
    l, p, v = map(int, input().split())
    if (l, p, v) == (0, 0, 0):
        break

    answers.append((v // p) * l + min(v % p, l))

for i, answer in enumerate(answers):
    print(f'Case {i + 1}: {answer}')