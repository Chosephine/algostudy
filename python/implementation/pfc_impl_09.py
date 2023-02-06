# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 2회차 풀이(string 디렉토리에 있음)
# 프로그래머스에서 풀다가 디버그 힘들어서 한시간 걸림ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ ㅠ

def check(s, l_s, unit):
    new = ''
    cur_idx = 0
    this = s[cur_idx: cur_idx + unit]
    this_cnt = 1

    while cur_idx + (unit * 2) <= l_s + 1:
        # print(this)
        if this == s[cur_idx + unit: cur_idx + (unit * 2)]:
            this_cnt += 1
        else:
            if this_cnt == 1:
                new = new + this
            else:
                new = new + str(this_cnt) + this
            this_cnt = 1
        cur_idx += unit
        this = s[cur_idx: cur_idx + unit]
        # print(this)

    if this_cnt > 1:
        new = new + str(this_cnt) + s[cur_idx:]
    else:
        new = new + s[cur_idx:]
    #print(new)
    return len(new)


def solution(s):
    len_s = len(s)
    result = len_s
    for l in range(len_s // 2, 0, -1):  # 많이 묶을 수 있을 때 최저일 수 있을 것 같아서 break 걸려고 이렇게 만들어 봤는데 안되더라~
        this_len = check(s, len_s, l)
        if this_len < result:
            result = this_len
            break
    return result
