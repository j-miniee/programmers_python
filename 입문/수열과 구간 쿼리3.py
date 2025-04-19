def solution(arr, queries):
    result = []
    for s, e, k in queries:
        min_value = 1000000
        found = False

        for i in range(s, e+1):
            if arr[i] > k:
                if min_value > arr[i]:
                    min_value = arr[i]
                found = True

        if found:
            result.append(min_value)
        else:
            result.append(-1)

    return result

'''
 s  e  k
[2, 4, 5],  2<=i<=4, (i:2, 3, 4)   | arr[i] > 5
[0, 3, 1],  0<=i<=3, (i:0, 1, 2, 3)| arr[i] > 1
[2, 3, 2],  2<=i<=3, (i:2, 3)      | arr[i] > 2
'''

print(solution( [1, 2, 3, 4, 5, 6], [[2, 4, 5], [0, 3, 1], [2, 3, 2]]))# [-1, 2, 3]
print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))# [3, 4, -1]

