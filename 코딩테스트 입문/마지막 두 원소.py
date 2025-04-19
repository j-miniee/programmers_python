def solution(num_list):
    n_len = len(num_list) -1

    if num_list[n_len] > num_list[n_len-1]:
        num_list.append(num_list[n_len] - num_list[n_len-1])
    else:
         num_list.append(num_list[n_len]*2)

    return num_list
        


print(solution([2, 1, 6]))
print(solution([5, 2, 1, 7, 5]))
# print(solution())