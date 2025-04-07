def solution(l, r):
    answer = []


    n = 5
    if l <= n:
        answer.append(n)

    while True:
        for i in ('0', '5'):
            if n <= r:
                n = int(str(n) + i)
                if l<= n <= r:
                    answer.append(n)
            else:
                break

    if not answer:
        return [-1]

    return answer


print(solution(5, 555)) # [5, 50, 55, 500, 505, 550, 555]
# print(solution(10, 20)) # [-1]
# l= 10, r = 55