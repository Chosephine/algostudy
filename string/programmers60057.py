# 2020 KAKAO BLIND RECRUITMENT 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    s_len = len(s)
    answer = s_len
    for n in range(1, (s_len // 2) + 1):
        result = ''
        # print(result)
        cnt = 1
        for i in range(0, s_len, n):
            # print(i)
            if i + n < s_len:
                if s[i:i + n] == s[i + n : i + 2 * n]:
                    cnt += 1
                else:
                    if cnt == 1:
                        result += f'{s[i:i+n]}'
                    else:
                        result += f'{cnt}{s[i:i+n]}'
                        cnt = 1
            else:
                if cnt == 1:
                    result += f'{s[i:]}'
                else:
                    result += f'{cnt}{s[i:]}'
                    cnt = 1
                break
        # print(result)
        if answer > len(result):
            answer = len(result)

    return answer

s = "xababcdcdababcdcd"
print(solution(s))