def calc_date(day):
    y, m, d = map(int, day.split('.'))
    
    return y * 12 * 28 + m * 28 + d
    
def solution(today, terms, privacies):
    answer = []
    today = calc_date(today)
    t = {i.split()[0] : int(i.split()[1]) * 28 for i in terms}
    
    for i, p in enumerate(privacies):
        date = p.split()[0]
        kind = p.split()[1]
        d = calc_date(date)
        d = d + int(t[kind])
        
        if today >= d:
            answer.append(i + 1)
    
    return answer