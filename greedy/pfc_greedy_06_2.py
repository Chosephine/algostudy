# programmers42891 2019 KAKAO 무지의 먹방 라이브

def solution(food_times, k):
    cycle = 0
    table_size = len(food_times)
    answer = 0
    while min(food_times) * table_size <= k:
        for food in food_times:
            food -= min(food_times)




    return answer + q

print(solution([3, 1, 2], 5))