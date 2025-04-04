def solution(arr, queries):
    
    for i in range(len(queries)):
        idx0 = queries[i][0] #0
        idx1 = queries[i][1] #3
        arr[idx0], arr[idx1] = arr[idx1], arr[idx0]

    return arr

def solution2(arr, queries):
    for idx0, idx1 in queries:
        arr[idx0], arr[idx1] = arr[idx1], arr[idx0]
    return arr

print(solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]]))


