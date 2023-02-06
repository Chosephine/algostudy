# programmers42891 2019 KAKAO 무지의 먹방 라이브
# 정확성 37.5 / 효율성 0.0

def solution(food_times, k):
    len_food = len(food_times)
    cnt_food = food_times
    answer = 0
    for n in range(k):
        if cnt_food[answer]:
            cnt_food[answer] -= 1
            answer = (answer + 1) % len_food
        else:
            while not cnt_food[answer]:
                answer = (answer + 1) % len_food
            cnt_food[answer] -= 1
            answer = (answer + 1) % len_food

    if not cnt_food[answer]:
        cnt_zero = 0
        while not cnt_food[answer]:
            if cnt_zero == len_food:
                answer = -1
            answer = (answer + 1) % len_food
            cnt_zero += 1

    return answer + 1

print(solution([3, 1, 2], 5))