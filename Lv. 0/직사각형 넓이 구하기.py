def solution(dots):
    answer = 0

    x, y= [], []
    for d in dots:
        x.append(d[0])
        y.append(d[1])

    answer = (max(x)-min(x)) * (max(y)-min(y))

    return answer

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]	))

print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))