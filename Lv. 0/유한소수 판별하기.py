import math

def solution(a, b):
    gcd = math.gcd(a,b)
    b = b // gcd
    
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
    
    return 1 if b == 1 else 2

print(solution(7,20)) #1
print(solution(11,22)) #1
print(solution(12,21)) #2
