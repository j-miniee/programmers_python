def solution(arr, queries):
    
    for s, e, k in queries:
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1


    return arr

print(solution([0, 1, 2, 4, 3], [[0, 4, 1],[0, 3, 2],[0, 3, 3]]))

'''
 s  e  k        i가 k의 배수이면 arr[i] += 1
[0, 4, 1] 0<=i<=4 (i: 0, 1, 2, 3, 4) k=1
[0, 3, 2] 0<=i<=3 (i: 0, 1, 2, 3)    k=2
[0, 3, 3] 0<=i<=3 (i: 0, 1, 2, 3)    k=3
'''