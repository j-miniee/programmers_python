def solution(babbling):
    sound = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for b in babbling:
        tmp = b
        for s in sound:
            tmp = tmp.replace(s, " ")
        if tmp.strip() == "":
            cnt += 1

    return cnt


print(solution(["aya", "yee", "u", "maa", "wyeoo"])) #1
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])) #3