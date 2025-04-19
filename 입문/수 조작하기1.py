def solution(n, control):
    con = {'w': 1,'s':-1,'d':10,'a':-10}
    
    for i in control:
        n += con[i]
    return n


print(solution(0, "wsdawsdassw")) #-1
