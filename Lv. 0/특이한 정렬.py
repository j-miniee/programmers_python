def solution(numlist, n):
    result = []

    for num in numlist:
        inserted = False
        d1 = abs(num - n)
        for i, r in enumerate(result):
            d2 = abs(r - n)
            if d1 < d2 or (d1==d2 and num > r):
                result.insert(i, num)
                inserted = True
                break

        if not inserted:
            result.append(num)
    
    return result

print(solution([1, 2, 3, 4, 5, 6], 4)) # [4, 5, 3, 6, 2, 1]
print(solution([10000,20,36,47,40,6,10,7000], 30)) # [36, 40, 20, 47, 10, 6, 7000, 10000]
