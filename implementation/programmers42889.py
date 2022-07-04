# 2019 KAKAO BLIND RECRUITMENT 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    # idx 0은 버리고, idx 1~N+1까지 이용
    game_map = [0] * (N + 2)
    for stage in stages:
        for i in range(stage):
            game_map[i] += 1
    # print(game_map)
    new_game_map = [0] * (N + 2)
    for i in range(1, N + 2):
        if game_map[i-1] == 0:
            new_game_map[i] = (0, i)
        else:
            new_game_map[i] = ((game_map[i-1] - game_map[i]) / game_map[i-1], i)
    new_game_map.pop(0)
    new_game_map.pop()
    new_game_map.sort(key = lambda x : (-x[0], x[1]))
    # print(new_game_map)
    answer = list(map(lambda x: x[1], new_game_map))
    return answer


N_sample = 5
stages_sample = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N_sample, stages_sample))