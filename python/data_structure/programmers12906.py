# 프로그래머스 12906 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    answer.append(arr[0])

    for n in arr:
        if answer[-1] != n:
            answer.append(n)

    return answer