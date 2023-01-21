def solution(array, commands):
    answer = []
    
    for comm in commands:
        i = comm[0] - 1
        j = comm[1]
        idx = comm[2]
        temp = [array[n] for n in range(i, j)]
        temp.sort()
        answer.append(temp[idx - 1])

    print('answer', answer)
        
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))     #	[5, 6, 3]