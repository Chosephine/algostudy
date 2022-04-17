# 2022 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    N = len(id_list)
    id_dict = {}
    for i in range(N):
        id_dict[id_list[i]] = i

    # 2차원 배열
    # r: 신고한 id / c: 신고 받은 id
    reports = [[0] * N for _ in range(N)]
    for r in report:
        fr, to = r.split()
        reports[id_dict[fr]][id_dict[to]] = 1

    cnts = []
    for c in range(N):
        temp = 0
        for r in range(N):
            temp += reports[r][c]
        cnts.append(temp)

    suspended = []
    for j in range(N):
        if cnts[j] >= k:
            suspended.append(j)

    answer = [0] * N
    for k in suspended:
        for r in range(N):
            if reports[r][k]:
                answer[r] += 1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
