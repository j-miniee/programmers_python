def solution(spell, dic):
    for d in dic:
        for i, s in enumerate(spell):
           if d.count(s) != 1:
               break
        #    if i == len(spell)-1:
        #        return 1
        else:
            return 1
    return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])) #2
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"])) #1
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"])) #2