def solution(num_list):
    total = 1
    for n in num_list:
        total *= n

    sum_squared = sum(num_list) **2

    return 1 if total < sum_squared else 0
        


print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))