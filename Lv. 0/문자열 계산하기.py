def solution(my_string):
    n_list = my_string.split()
    answer = int(n_list[0])

    for i in range(1, len(n_list), 2):
        if n_list[i] == '+':
            answer += int(n_list[i+1])
        elif n_list[i] == '-':
            answer -= int(n_list[i+1])

    return answer

print(solution("3 + 4 - 5"))