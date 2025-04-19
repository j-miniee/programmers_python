def solution(n1, d1, n2, d2):
    n = n1*d2 +n2*d1
    d = d1*d2
    
    for i in range(min(n,d), 0, -1):
        if n % i == 0 and d % i == 0:
            d = d // i
            n = n // i
    
    return  [n, d]


def solution3(n1, d1, n2, d2):
    n = n1*d2 +n2*d1
    d = d1*d2
    
    remainder = n % d
    quotient = n // d
    
    if d % remainder == 0: #오류 발생
        d  = d // remainder
        n = quotient * d +1

    return  [n, d]

print(solution(1,2,1,3))

print(solution3(1,2,1,3)) #성공
# print(solution3(2,4,2,4)) #예외(remainder=0으로 못 나눔) 