def solution(code):
    answer = ''
    mode = 0

    for i in range(len(code)):
        if code[i] == '1':
            if mode == 0:
                mode = 1
            else:
                mode = 0
            continue
    
        if mode == 0 and i%2 == 0:
            answer += code[i]
        elif mode == 1 and i%2 != 0:
            answer += code[i]
        
    if answer == '':
            return "EMPTY"

    return answer


print(solution("abc1abc1abc")) #acbac
print(solution(""))