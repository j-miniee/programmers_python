def solution(dots):
    a, b, c, d = dots

    if (a[0]-b[0]) * (c[1]-d[1]) == (a[1]-b[1]) * (c[0]-d[0]):
        return 1
    elif (a[0]-c[0]) * (b[1]-d[1]) == (a[1]-c[1]) * (b[0]-d[0]):
        return 1
    elif (a[0]-d[0]) * (b[1]-c[1]) == (a[1]-d[1]) * (b[0]-c[0]):
        return 1
    
    return 0

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]])) #1
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]])) #0