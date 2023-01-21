def solution(sizes):
    w = 0
    h = 0
    
    for s in sizes:   
        # 둘중 작은걸 w로, 큰걸 h로
        if s[0] < s[1]:
            s_w = s[0]
            s_h = s[1]
        else:
            s_w = s[1]
            s_h = s[0]

        if w < s_w:
            w = s_w
        if h < s_h:
            h = s_h
    
    return w * h

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))               # 4000 (80 * 50)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))          # 120 (8*15)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))          # 133 (19*7)