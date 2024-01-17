# 백준 2579 계단 오르기
# https://www.acmicpc.net/problem/2579

def max_score(n: int, score_list: list) -> int:
    # 사용할 자료구조
    score_list = [0] + score_list
    cumulated_score = [[] for _ in range(n + 1)]

    # 초기화
    cumulated_score[0].append((score_list[0], 1))

    for i in range(n):
        for score_tuple in cumulated_score[i]:
            score, history = score_tuple

            if history >= 2 and i != 1:
                if i + 2 < n + 1 :
                    # 한칸 이동 불가
                    cumulated_score[i + 2].append((score + score_list[i + 2], 1))

            else:
                # 한칸 이동 및 두칸 이동 모두 가능
                if i + 1 < n + 1:
                    cumulated_score[i + 1].append((score + score_list[i + 1], history + 1))
                if i + 2 < n + 1:
                    cumulated_score[i + 2].append((score + score_list[i + 2], 1))

    return max(cumulated_score[-1])[0]


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())

    stairs = list(int(input()) for _ in range(N))

    answer = max_score(N, stairs)

    print(answer)

