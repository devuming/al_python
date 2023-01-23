
def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        i = 0
        last = ''   # 연속해서 같은 발음 불가능
        
        while i < len(bab):
            if len(bab[i:]) < 2: break
            if last == bab[i:i+2] or last == bab[i:i+3] : break
            if bab[i:i+2] in can:
                last = bab[i:i+2]
                i = i + 2
            elif bab[i:i+3] in can:
                last = bab[i:i+3]
                i = i + 3
            else:
                break
        if i == len(bab):
            answer += 1
            
    return answer

print(solution(["aya", "yee", "u", "maa"])) # 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))	#2
print(solution(["ayaaya", "uuuu", "maa", "mawooma"]))	#1