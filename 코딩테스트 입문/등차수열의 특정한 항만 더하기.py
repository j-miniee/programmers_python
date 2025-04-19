def solution(a, d, included):
    total = 0
    
    for b in included:
        if b:
            total += a
        a += d
    
    return total

print(solution(3, 4, [True, False, False, True, True]))
print(solution(7, 1, [False, False, False, True, False, False, False]))

