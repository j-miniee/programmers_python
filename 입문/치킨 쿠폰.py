def solution(coupon):
    chicken = 0
    while coupon >= 10:
        quotient = coupon // 10 
        chicken += quotient  
        coupon = quotient + (coupon %10)

    return chicken

print(solution(100))
print(solution(1081))