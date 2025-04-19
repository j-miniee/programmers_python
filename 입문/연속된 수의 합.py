def solution(num, total):
    avg = total // num
    
    if num % 2 != 0:
        answer = [i for i in range(avg- (num-1)//2, avg+(num+1)//2)]
    else:
        answer = [i for i in range(avg- (num-1)//2, avg+(num+2)//2)]

    
    return answer

print(solution(3, 12)) #[3, 4, 5]
print(solution(5, 15)) #[1, 2, 3, 4, 5]
print(solution(4, 14)) #[2, 3, 4, 5]
print(solution(5, 5)) #[-1, 0, 1, 2, 3]
