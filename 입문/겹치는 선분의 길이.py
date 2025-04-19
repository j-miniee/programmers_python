def solution(lines):
    a, b, c = lines

    # 선분이 차지하는 구간을 set으로 표현 (끝점 포함 X → 거리 기준)
    a_set = set(range(a[0], a[1]))
    b_set = set(range(b[0], b[1]))
    c_set = set(range(c[0], c[1]))

    # 겹치는 구간 계산
    ab = a_set & b_set
    bc = b_set & c_set
    ac = a_set & c_set

    # 전체 겹치는 구간 (중복 제거)
    total = ab | bc | ac

    return len(total)

print(solution([[0, 1], [2, 5], [3, 9]])) #2
print(solution([[-1, 1], [1, 3], [3, 9]])) #0
print(solution([[0, 5], [3, 9], [1, 10]])) #8
