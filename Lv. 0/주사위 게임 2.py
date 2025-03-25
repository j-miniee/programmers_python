def solution(a, b, c):
    dice = [a, b, c]
    cnt = len(set(dice))

    sum1 = a+b+c
    sum2 = a**2 + b**2 + c**2
    sum3 = a**3 + b**3 + c**3

    if cnt == 3:
       return  sum1
    elif cnt == 2:
        return  sum1 * sum2
    elif cnt == 1:
        return  sum1 * sum2 *sum3



print(solution(2, 6, 1)) #9 (3, 3, 5)
print(solution(5, 3, 3,)) #473
print(solution(4, 4, 4)) #110592
