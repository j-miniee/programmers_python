def solution(array):
    
    counts={}
    idx = set(array) # 1, 2, 3, 4
    
    for i in idx:
        counts[i] = array.count(i)

    values = list(counts.values())
    max_values = max(values)
    if values.count(max_values) > 1:
        return -1
        
    for k in counts.keys():
        if counts[k] == max_values:
            return k

print(solution([1, 2, 3, 3, 3, 4])) #3
print(solution([1, 1, 2, 2])) #-1