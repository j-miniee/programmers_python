def solution(A, B):
    if A == B:
        return 0
    
    A = list(A)
    cnt = 0
    
    for _ in range(len(A)):
        last = A.pop()
        A = [last] + A
        cnt += 1
        if A == list(B):
            return cnt
        
    return -1

print(solution("hello", "ohell")) #1
print(solution("apple", "elppa")) #-1
print(solution("atat", "tata")) #1