def solution(polynomial):
    x_coef, const = 0, 0

    terms = polynomial.split(" + ")


    for term in terms:
        if 'x' in term:
            n = term.replace('x', '')
            if n == '':
                x_coef += 1
            else:
                x_coef += int(n)
        else:
            const += int(term)

    result = ''

    if x_coef: #0이 아닐 때만 실행
        if x_coef == 1:
            result += 'x'
        else:
            result += str(x_coef) + 'x'

    if const :
        if result:
            result += ' + '
        result+= str(const)

    return result

print(solution("3x + 7 + x")) #"4x + 7"
print(solution("x + x + x")) #"3x"
print(solution("x + 5")) #x +5
print(solution('1')) # 1