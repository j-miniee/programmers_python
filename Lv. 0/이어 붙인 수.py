def solution(num_list):
    odd, even = '', ''

    for n in num_list:
        if n % 2 == 0:
            even += str(n)
        else:
            odd += str(n)

    return int(even) + int(odd)


print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))