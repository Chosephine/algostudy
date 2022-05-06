# 2021 KAKAO BLIND RECRUITMENT 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def make_course(candidates, cnt, orders):
    checks = combinations(candidates, cnt)
    result = []
    cnt_max = 0
    # print(list(checks))
    for check in checks:
        cur_max = 0
        for order in orders:
            if len(order) >= cnt:
                for i in range(cnt):
                    if check[i] in order:
                        continue
                    else:
                        break
                else:
                    cur_max += 1
        if cur_max > cnt_max:
            if cur_max >= 2:
                cnt_max = cur_max
                result = [''.join(check)]
        elif cur_max == cnt_max:
            if cur_max >= 2:
                result.append(''.join(check))
    # print(result)
    return result



def solution(orders, course):
    answer = []
    menus = set()
    max_order_len = 0
    for order in orders:
        for a in order:
            menus.add(a)
        max_order_len = max(max_order_len, len(order))
    menus = list(menus)
    menus.sort()
    for num in course:
        if num <= max_order_len:
            answer += make_course(menus, num, orders)
        else:
            pass
    answer.sort()
    print(answer)
    # return answer
    return


o = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
c = [2, 3, 5]

solution(o, c)