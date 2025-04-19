def solution(c):
    differ = c[1] - c[0]

    if c[0] != 0 and c[2] != c[1] + differ:
        ratio = c[1] // c[0]
        if c[2] == c[1] * ratio:
            return c[-1] *ratio

    return c[-1] + differ



print(solution([1, 2, 3, 4])) #5
print(solution([2, 4, 8])) #16