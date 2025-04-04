def solution(arr, queries):
    result = []
    for query in queries:
        s, e, k = query[0],query[1],query[2]
        min_value = 1000000
        found = False

        if s < k:
            for i in range(k+1, e+1): #3, 4
                if min_value > arr[i]:
                    min_value = arr[i]
                found = True

        elif s > k:
            for i in range(s, e+1): #3
                if min_value > arr[i]:
                    min_value = arr[i]
                found = True
        if found:
            result.append(min_value)
        else:
            result.append(-1)

    return result

'''
입력값 〉 [1, 2, 3, 4, 5, 6], [[2, 4, 5], [0, 3, 1], [2, 3, 2]]
기댓값 〉 [-1, 2, 3]
'''

print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))
# [3, 4, -1]

print(solution( [1, 2, 3, 4, 5, 6], [[2, 4, 5], [0, 3, 1], [2, 3, 2]]))
