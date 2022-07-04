def solution(numbers, hand):
    answer = ''
    location = {'left':[3, 0], 'right':[3, 2]}    # 손가락 현재 위치
    key = [[1, 2, 3]
          ,[4, 5, 6]
          ,[7, 8, 9]
          ,['*', 0, '#']]
    
    for n in numbers:
        if n == 1: 
            row = 0
            col = 0
        elif n == 0:
            row = 3
            col = 1
        else:
            row = (n - 1) // 3
            col = (n - 1) - row * 3
        
        n_loc = [row, col]      # 누를 숫자

        if n in [1, 4, 7] :         # 왼손
            answer += 'L'
            location['left'] = n_loc
        elif n in [3, 6, 9]:       # 오른손
            answer += 'R'
            location['right'] = n_loc
        else :                      # 중앙   
            dis_left = abs(location['left'][0] - n_loc[0]) + abs(location['left'][1] - n_loc[1])      # 왼손 거리
            dis_right = abs(location['right'][0] - n_loc[0]) + abs(location['right'][1] - n_loc[1])   # 오른손 거리

            if dis_left < dis_right :
                answer += 'L'
                location['left'] = n_loc
            elif dis_left > dis_right :
                answer += 'R'
                location['right'] = n_loc
            else:
                # 거리가 같은 경우            
                answer += 'R' if hand == 'right' else 'L'
                location[hand] = n_loc            
                
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))     # "LRLLLRLLRRL" 
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))      # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))        # 	"LLRLLRLLRL"n
