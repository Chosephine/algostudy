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


# 정확성 58.3, 효율성 41.7
def solution3(participant, completion):

    dict_participant = dict()
    hash_sum = 0

    # hash() : 객체의 해시값을 반환 (해시가 있는 경우). 해시값은 정수.
    # 딕셔너리 조회 중에 딕셔너리 키를 빨리 비교하는 데 사용
    # 같다고 비교되는 숫자 값은 같은 해시값을 갖습니다 (1과 1.0의 경우와 같이 형이 다른 경우조차도 그러함).

    for player in participant:
        hashed_player = hash(player)
        dict_participant[hashed_player] += player
        hash_sum += hashed_player

    for player in completion:
        hash_sum -= hash(player)

    return dict_participant[hash_sum]