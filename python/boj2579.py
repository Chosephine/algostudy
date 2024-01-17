# 백준 2579 계단 오르기
# https://www.acmicpc.net/problem/2579

def max_score(n: int, score_list: list) -> int:
    # 사용할 자료구조
    score_list = [0] + score_list
    cumulated_score = [0] * (n + 1)
    histories = [0] * (n + 1)

    # 초기화
    cumulated_score[0] = score_list[0]
    histories[0] = 1

    for i in range(n):
        # 이번 계단에서 다음 계단으로 넘어갈 때 계산

        # 두칸 건너 뛸 땐 histories 1로 설정
        # 한칸 건너 뛸 땐 histories 에 1 추가
        if histories[i] >= 2 and i != 1:
            if i + 2 < n + 1 and cumulated_score[i + 2] < cumulated_score[i] + score_list[i + 2]:
                # 한칸 이동 불가
                cumulated_score[i + 2] = cumulated_score[i] + score_list[i + 2]
                histories[i + 2] = 1

        else:
            # 한칸 이동 및 두칸 이동 모두 가능
            if i + 1 < n + 1 and cumulated_score[i + 1] < cumulated_score[i] + score_list[i + 1]:
                cumulated_score[i + 1] = cumulated_score[i] + score_list[i + 1]
                histories[i + 1] = histories[i] + 1
            if i + 2 < n + 1 and cumulated_score[i + 2] < cumulated_score[i] + score_list[i + 2]:
                cumulated_score[i + 2] = cumulated_score[i] + score_list[i + 2]
                histories[i + 2] = 1

    return cumulated_score[-1]


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())

    stairs = list(int(input()) for _ in range(N))

    answer = max_score(N, stairs)

    print(answer)

