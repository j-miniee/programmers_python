def solution(quiz):
    answer = []

    for eq in quiz:
        eq_list = eq.split()
        
        result = int(eq_list[0])
        for i in range(1, len(eq_list), 2):
            if eq_list[i] == '+':
                result += int(eq_list[i+1])
            elif eq_list[i] == '-':
                result -= int(eq_list[i+1])

        if str(result) == eq_list[len(eq_list)-1]:
            answer.append('O')
        else:
            answer.append('X')

    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))