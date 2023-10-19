# 프로그래머스 42576 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 정확성 58.3, 효율성 0.0
def solution1(participant, completion):
    # participant : 마라톤에 참여한 선수들의 이름
    # completion : 완주한 선수들의 이름이 담긴 배열
    # answer : 완주하지 못한 선수의 이름

    for player in completion:
        participant.remove(player)

    answer = participant[0]

    return answer

# 정확성 58.3, 효율성 0.0
def solution2(participant, completion):

    dict_participant = dict()
    keys = []

    for player in participant:
        if player in keys:
            dict_participant[player] += 1
        else:
            dict_participant[player] = 1
            keys.append(player)

    for player in completion:
        dict_participant[player] -= 1

    for k in keys:
        if dict_participant[k] == 1:
            return k

    return keys