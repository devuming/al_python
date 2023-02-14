def toMinute(time):
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

def solution(book_time):
    answer = 0
    book_time.sort(key = lambda x:x[0])
    room = []
    
    for i, book in enumerate(book_time):
        for j in range(len(room)):
            if toMinute(book[0]) >= toMinute(room[j][1]) + 10:
                room.pop(j)
                break
        room.append(book)
        
    return len(room)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])) # 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]])) # 1
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])) # 3