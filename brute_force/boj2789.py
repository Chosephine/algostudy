# boj2789 블랙잭
# https://www.acmicpc.net/problem/2798

# 3개 조합 재귀로 찾아서, 최대합일 경우 답 갱신

N, M = map(int, input().split())
cards = list(map(int, input().split()))
used = [0] * N
result = 0


def combination(cnt, part_sum):
    global N, M, result
    # 가지치기
    if part_sum > M:
        return

    # 조합 완성(재귀 종료 조건)
    if cnt == 3:
        print(part_sum, result)
        if part_sum > result:
            result = part_sum
        return
    else:
        for i in range(N):
            if not used[i]:
                used[i] = 1
                combination(cnt+1, part_sum+cards[i])
                used[i] = 0


combination(0, 0)

print(result)