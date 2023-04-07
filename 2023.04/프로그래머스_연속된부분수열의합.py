def solution(sequence, k):
    answer = []
    for i in range(1, len(sequence)):
        sequence[i] = sequence[i-1] + sequence[i]
        
    start, end = 0, len(sequence) - 1
    i, j = 0, 0
    while i <= j and j < len(sequence):
        if i > 0:
            sub_sum = sequence[j] - sequence[i - 1]
        else:
            sub_sum = sequence[j]
            
        if sub_sum == k:
            if j - i + 1 < end - start + 1:
                start = i
                end = j
            i += 1
        elif sub_sum < k:
            j += 1
        else:
            i += 1
        
    return [start, end]