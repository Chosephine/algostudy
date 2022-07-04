# 프로그레머스 Greedy 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for student in range(1, n+1):
        if student in lost:
            if student in reserve:
                answer += 1
                reserve.remove(student)
            elif student - 1 in reserve:
                answer += 1
                reserve.remove(student - 1)
            elif student + 1 in reserve:
                if student + 1 in lost:
                    pass
                else:
                    answer += 1
                    reserve.remove(student + 1)
        else:
            answer += 1
    return answer