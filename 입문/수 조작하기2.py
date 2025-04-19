def solution(numLog):
    n = numLog[0]
    result = ''
    control = {1:'w',-1:'s',10:'d',-10:'a'}

    for i in range(1, len(numLog)):
        c_key = numLog[i] - n
        result += control[c_key]
        n = numLog[i]
    return result



print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1])) # "wsdawsdassw"