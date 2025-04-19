def solution(score):
    avg=[sum(s)/ 2 for s in score]
    
    rank_dict = {}
    avg_sort = sorted(avg, reverse=True)
    for i, a in enumerate(avg_sort):
        if a not in rank_dict: 
            rank_dict[a] = i+1

    result = [rank_dict[a] for a in avg]

    return result

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], 
                [100, 90], [100, 100], [10, 30]]))
# print(solution())
