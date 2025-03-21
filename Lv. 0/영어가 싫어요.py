def solution(numbers):

    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
               'seven', 'eight', 'nine']

    answer = ""    
    tmp = ""
    for i in range(len(numbers)):
        tmp += numbers[i]
        if tmp in num_list:
            answer += str(num_list.index(tmp))
            tmp = ""

    return int(answer)

# 방법2)
# def solution(numbers):
#     d = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
#          'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
#     for k,v in d.items():
#         numbers = numbers.replace(k,v)
#     return int(numbers)