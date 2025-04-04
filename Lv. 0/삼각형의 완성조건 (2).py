def solution(sides):
    count = 0

    #1) 가장 긴 변이 6인 경우(max(sides)인 경우)
    # 가장 긴 변의 길이 < n1 + n2(나머지 두 변)
    n_side = min(sides) 
    m_side = max(sides) 
    for n in range(m_side-n_side, m_side):
        count += 1 

    #2)나머지 한 변이 긴 변인 경우
    n_side = max(sides) 
    m_side = max(sides) + min(sides) 
    for n in range(n_side+1, max(sides) + min(sides)):
        count += 1

    return count




print(solution([1, 2])) #1
print(solution([3, 6])) #5
print(solution([11, 7])) #13

# n_side = 7, m_side = 11
# count = 7#4,5,6,7,8,9,10

