# https://school.programmers.co.kr/learn/courses/30/lessons/42889
# 이코테 기출 25, 프로그래머스 42889
# 2회차 풀이(implementation.programmers42889.py)... 더 비효율적인 코드가 되었다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

def solution(N, stages):
    # idx 0은 버리기
    # idx N+2는 all clear
    reach_not_clear = [0] * (N + 2)
    reach = [0] * (N + 2)

    for stage in stages:
        reach_not_clear[stage] += 1
        for i in range(stage + 1):
            reach[i] += 1

    ratio = []
    for j in range(1, N + 1):
        if not reach[j]:
            ratio.append((j, 0))
        else:
            ratio.append((j, reach_not_clear[j] / reach[j]))
    ratio.sort(key=lambda x: (-x[1], x[0]))

    answer = []
    for r in ratio:
        answer.append(r[0])
    # return reach_not_clear, reach, ratio
    return answer


# N_sample = 5
# stages_sample = [2, 1, 2, 6, 2, 4, 3, 3]
N_sample = 4
stages_sample = [4,4,4,4,4]

print(solution(N_sample, stages_sample))
