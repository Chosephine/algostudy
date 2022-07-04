# 프로그래머스 2017 팁스다운 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

# def solution(s):
#     str = s
#     answer = 1
#     flag = True
#     while str and flag:
#         # print(str)
#         for i in range(1, len(str)):
#             if str[i] == str[i-1]:
#                 str = str[:i-1] + str[i+1:]
#                 break
#         else:
#             flag = False
#             answer = 0
#     return answer

def solution(s):
    stack = []
    str = s
    while str and flag:
        # print(str)
        for i in range(1, len(str)):
            if str[i] == str[i-1]:
                str = str[:i-1] + str[i+1:]
                break
        else:
            flag = False
            answer = 0
    return answer

print(solution('baabaa'))